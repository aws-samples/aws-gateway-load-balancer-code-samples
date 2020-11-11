Following example shows how to create VPC Endpoint Service using Gateway Load Balancer ARN using [ec2 create-vpc-endpoint-service-configuration](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpc-endpoint-service-configuration.html) command using AWS CLI version 1. Replace the parameter values inside '< >' with appropriate values.

* Command:

```bash
aws ec2 create-vpc-endpoint-service-configuration \
    --gateway-load-balancer-arns <gwlb_arn> \
    --no-acceptance-required
```

* Output:

```bash
{
    "ServiceConfiguration": {
        "ServiceType": [
            {
                "ServiceType": "GatewayLoadBalancer"
            }
        ],
        "ServiceId": "vpce-svc-xxxx",
        "ServiceName": "com.amazonaws.vpce.us-west-2.vpce-svc-xxxx",
        "ServiceState": "Available",
        "AvailabilityZones": [
            "us-west-2a",
            "us-west-2b"
        ],
        "AcceptanceRequired": false,
        "ManagesVpcEndpoints": false,
        "GatewayLoadBalancerArns": [
            "arn:aws:elasticloadbalancing:us-west-2:xxxxxxxxxxxx:loadbalancer/gwy/cli-gwlb1/dabd816b54d028e1"
        ]
    }
}
```

