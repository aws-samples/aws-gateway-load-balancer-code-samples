Following example shows how to create Gateway Load Balancer Endpoint using VPC Endpoint Service Name using [ec2 create-vpc-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpc-endpoint.html) command. Replace the parameter values inside '< >' with appropriate values. Only one subnet per GWLBe is supported.

* Command

```bash
aws ec2 create-vpc-endpoint \
    --vpc-endpoint-type GatewayLoadBalancer \
    --vpc-id <spoke-vpc-id> \
    --subnet-ids <gwlbe-subnet-xxxx> \
    --service-name <vpce-service-name>
```

* Output:

```bash
{
    "VpcEndpoint": {
        "VpcEndpointId": "vpce-1xxx",
        "VpcEndpointType": "GatewayLoadBalancer",
        "VpcId": "vpc-xxxx",
        "ServiceName": "com.amazonaws.vpce.us-west-2.vpce-svc-xxxx",
        "State": "pending",
        "SubnetIds": [
            "subnet-xxxx"
        ],
        "RequesterManaged": false,
        "NetworkInterfaceIds": [
            "eni-xxxx"
        ],
        "CreationTimestamp": "2020-11-11T02:49:15.638Z",
        "OwnerId": "xxxxxxxxxxxx"
    }
}
```