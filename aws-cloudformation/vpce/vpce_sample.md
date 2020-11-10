* Following example shows how to create Gateway Load Balancer vpc endpoint using VPC endpoint service name using AWS CloudFormation. Template also adds endpoint as next-hop to respecitve route tables.

```yaml
AWSTemplateFormatVersion: '2010-09-09'

Description: >-
  This template creates an Gateway Load Balancer VPC Endpoint.

  **WARNING** This template creates one gateway load balancer endpoint associated with two public
  subnets. You will be billed for the AWS resources used if you create a
  stack from this template.

Metadata:
  AWS::CloudFormation::Interface:
    ParameterGroups:
      - Label:
          default: Gateway Load Balancer Endpoint Configuration
        Parameters:
          - VpcId
          - VpceSubnetId
          - ServiceName
          - ApplicationRoutTableId
          - IgwRouteTableId
    ParameterLabels:
      VpcId:
        default: The ID of the VPC in which the gateway load balancer endpoint will be created
      VpceSubnetId:
        default: Subnet Id for AZ1 for Gateway Load Balancer VPC Endpoint
      ServiceName:
        default: The name of the endpoint service to create gateway load balancer endpoint for
      ApplicationRoutTableId:
        default: Appliaction route table id
      IgwRouteTableId:
        default: IGW route table id

Parameters:
  VpcId:
    Description: Select VPC Id in which gateway load balancer endpoint will be created
    Type: AWS::EC2::VPC::Id
    ConstraintDescription: Must be a valid VPC Id
  VpceSubnetId:
     Description: Select subnet id for AZ1 for gateway load balancer endpoint
     Type: AWS::EC2::Subnet::Id
     ConstraintDescription: Must be a valid subnet id
  ServiceName:
    Description: >-
      Enter the name of the service for which you want to create gateway load balancer endpoint.
      Example service name: com.amazonaws.vpce.us-west-2.vpce-svc-0a76331bc5d6cc4cd
    Type: String
    ConstraintDescription: Must be a valid service name
  ApplicationRoutTableId:
     Description: >-
        Enter application rtb id to add endpoint as the next-hop.
        Example: 'rtb-05e7a62f7e20df1e4'
     Type: String
     ConstraintDescription: Must be a valid route table id
  IgwRouteTableId:
     Description: >-
        Enter IGW rtb id to add endpoint as the next-hop.
        Example: 'rtb-05e7a62f7e20df1e4'
     Type: String
     ConstraintDescription: Must be a valid route table id

Resources:
  GwlbVpcEndpoint:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcId: !Ref VpcId
      ServiceName: !Ref ServiceName
      VpcEndpointType: GatewayLoadBalancer
      SubnetIds:
        - !Ref VpceSubnetId
  
  EditClientRouteTable:
    Type: AWS::EC2::Route
    DependsOn: GwlbVpcEndpoint
    Properties:
      DestinationCidrBlock: 0.0.0.0/0
      VpcEndpointId: !Ref GwlbVpcEndpoint
      RouteTableId: !Ref ApplicationRoutTableId    

  EditIgwRouteTable:
    Type: AWS::EC2::Route
    DependsOn: GwlbVpcEndpoint
    Properties:
      DestinationCidrBlock: 10.0.0.32/27
      VpcEndpointId: !Ref GwlbVpcEndpoint
      RouteTableId: !Ref IgwRouteTableId

Outputs:
  ScGwlbVpcEndpointId:
    Description: Gateway Load Balancer VPC Endpoint ID
    Value: !Ref GwlbVpcEndpoint  

```