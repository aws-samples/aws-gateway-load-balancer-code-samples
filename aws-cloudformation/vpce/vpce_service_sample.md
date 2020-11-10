* Following example shows how to vpc endpoint service using Gateway Load Balancer ARN using AWS CloudFormation. It also creates custom resource to output the service name.

```yaml
AWSTemplateFormatVersion: "2010-09-09"

Description: This template creates Amazon VPC Endpoint Service using ELB ARN

Metadata:
  AWS::CloudFormation::Interface:
    ParameterGroups:
      - Label:
          default: Endpoint Service Configuration
        Parameters:
          - ElbArn
          - ConnectionAcceptance
      - Label:
          default: Endpoint Service Permissions
        Parameters:
          - AwsAccountToWhitelist
    ParameterLabels:
      ElbArn:
        default: >-
          ELB Amazon Resource Names (ARNs)for your service.
      ConnectionAcceptance:
        default: >- 
          Indicate whether requests from service consumers to create an
          endpoint to your service must be accepted.
      AwsAccountToWhitelist:
        default: >-
          The Amazon Resource Names (ARN) of one or more principals (IAM users,
          IAM roles, and AWS accounts). Permissions are granted to the 
          principals in this list.

Parameters:
  ElbArn:
    Description: >- 
      Enter Elastic load balancer ARN for your service. Network and Gateway
      Load Balancer are the two supported types.
    Type: String
    ConstraintDescription: Must be a valid ELB ARN
  ConnectionAcceptance:
    Description: >-
      Acceptance required for endpoint connection or not. Select true or
      false to either acceptance required or acceptance not required 
      default is set to false: acceptance not required
    Default: "false"
    AllowedValues: ["true", "false"]
    Type: String
    ConstraintDescription: Must be true or false
  AwsAccountToWhitelist:
    Description: >-
      Enter ARN of one or more prinicapls: IAM user, IAM roles and AWS accounts.
      To grant permissions to all principals, specify an asterisk (*).
    Type: String
    Default: arn:aws:iam::558283194989:root
    ConstraintDescription: Must be a valid AWS ARN of one or more principals

Resources:
  VpcEndpointService:
    Type: AWS::EC2::VPCEndpointService
    Properties:
      GatewayLoadBalancerArns:
        - !Ref ElbArn
      AcceptanceRequired: !Ref ConnectionAcceptance
 
  VpcEndpointServicePermissions:
    Type: AWS::EC2::VPCEndpointServicePermissions
    Properties:
      AllowedPrincipals:
        - !Ref AwsAccountToWhitelist
      ServiceId: !Ref VpcEndpointService

  LambdaExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - lambda.amazonaws.com
            Action:
              - sts:AssumeRole
      Path: /
      Policies:
        - PolicyName: root
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - logs:CreateLogGroup
                  - logs:CreateLogStream
                  - logs:PutLogEvents
                Resource: arn:aws:logs:*:*:*
              - Effect: Allow
                Action:
                  - ec2:DescribeVpcEndpointServiceConfigurations
                  - ec2:DescribeVpcEndpointServicePermissions
                  - ec2:DescribeVpcEndpointServices
                Resource: "*"

  DescribeVpceService:
    Type: AWS::Lambda::Function
    Properties:
      Handler: "index.handler"
      Role: !GetAtt
        - LambdaExecutionRole
        - Arn
      Code:
        ZipFile: |
          import boto3
          import cfnresponse
          import json
          import logging
          def handler(event, context):
              logger = logging.getLogger()
              logger.setLevel(logging.INFO)
              responseData = {}
              responseStatus = cfnresponse.FAILED
              logger.info('Received event: {}'.format(json.dumps(event)))
              if event["RequestType"] == "Delete":
                  responseStatus = cfnresponse.SUCCESS
                  cfnresponse.send(event, context, responseStatus, responseData)
              if event["RequestType"] == "Create":
                  try:
                      VpceServiceId = event["ResourceProperties"]["Input"]
                  except Exception as e:
                      logger.info('VPC Endpoint Service Id retrival failure: {}'.format(e))
                  try:
                      ec2 = boto3.client('ec2')
                  except Exception as e:
                      logger.info('boto3.client failure: {}'.format(e))
                  try:
                      response = ec2.describe_vpc_endpoint_service_configurations(
                          Filters=[
                              {
                                  'Name': 'service-id',
                                  'Values': [VpceServiceId]
                              }
                          ]
                      )
                  except Exception as e:
                      logger.info('ec2.describe_vpc_endpoint_service_configurations failure: {}'.format(e))
                  ServiceName = response['ServiceConfigurations'][0]['ServiceName']
                  responseData['Data'] = ServiceName
                  responseStatus = cfnresponse.SUCCESS
                  cfnresponse.send(event, context, responseStatus, responseData)
      Runtime: python3.7
      Timeout: 30

  VpceServiceName:
    DependsOn: VpcEndpointService
    Type: Custom::DescribeVpcEndpointServiceConfigurations
    Properties:
      ServiceToken: !GetAtt DescribeVpceService.Arn
      Input: !Ref VpcEndpointService

Outputs:
  SpVpcEndpointServiceId:
    Description: VPC Endpoint Service ID
    Value: !Ref VpcEndpointService
  SpVpcEndpointServiceName:
    Description: VPC Endpoint Service Name. Required to create VPC Endpoint
    Value: !GetAtt VpceServiceName.Data
```