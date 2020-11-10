* Following example shows how to create Gateway Load Balancer Endpoint using VPC Endpoint Service name using AWS CloudFormation. 

```yaml
AWSTemplateFormatVersion: '2010-09-09'

Description: >-
  This template creates a Gateway Load Balancer VPC Endpoint.

  **WARNING** This template creates one gateway load balancer endpoint 
  associated with 1 subnet. You will be billed for the AWS resources used
  if you create a stack from this template.

Metadata:
  AWS::CloudFormation::Interface:
    ParameterGroups:
      - Label:
          default: Gateway Load Balancer Endpoint Configuration
        Parameters:
          - VpcId
          - VpceSubnetId
          - ServiceName
    ParameterLabels:
      VpcId:
        default: The ID of the VPC in which the Gateway Load Balancer endpoint will be created
      VpceSubnetId:
        default: Subnet Id for Gateway Load Balancer VPC Endpoint
      ServiceName:
        default: VPC Endpoint Service Name For Gateway Load Balancer Endpoint     

Parameters:
  VpcId:
    Description: Select VPC Id in which gateway load balancer endpoint will be created
    Type: AWS::EC2::VPC::Id
    ConstraintDescription: Must be a valid VPC Id
  VpceSubnetId:
     Description: Select subnet id for gateway load balancer endpoint, only one subnet per AZ
     Type: AWS::EC2::Subnet::Id
     ConstraintDescription: Must be a valid subnet id
  ServiceName:
    Description: >-
      Enter the name of the service for which you want to create gateway load balancer endpoint.
      Example service name: com.amazonaws.vpce.us-west-2.vpce-svc-0a76331bc5d6cc4cd
    Type: String
    ConstraintDescription: Must be a valid service name

Resources:
  GwlbVpcEndpoint:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcId: !Ref VpcId
      ServiceName: !Ref ServiceName
      VpcEndpointType: GatewayLoadBalancer
      SubnetIds:
        - !Ref VpceSubnetId

Outputs:
  GwlbVpcEndpointId:
    Description: Gateway Load Balancer VPC Endpoint ID
    Value: !Ref GwlbVpcEndpoint
```
