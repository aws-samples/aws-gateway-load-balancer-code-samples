Following example shows how to create AWS Gateway Load Balancer using
[elbv2 create-load-balancer](https://docs.aws.amazon.com/cli/latest/reference/elbv2/create-load-balancer.html) command using AWS CLI version 1. Replace the parameter values inside '< >' with appropriate values.

* Command: 

```bash
aws elbv2 create-load-balancer \
    --type gateway \
    --subnets <appliance-subnet1> <appliance-subnet2> \
    --name <gwlb1>
```

* Output:

```bash
{
    "LoadBalancers": [
        {
            "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-west-2:xxxxxxxxxxxx:loadbalancer/gwy/cli-gwlb1/dabd816b54d028e1",
            "CreatedTime": "2020-11-11T01:16:45.568Z",
            "LoadBalancerName": "cli-gwlb1",
            "VpcId": "vpc-xxxx",
            "State": {
                "Code": "provisioning"
            },
            "Type": "gateway",
            "AvailabilityZones": [
                {
                    "ZoneName": "us-west-2b",
                    "SubnetId": "subnet-1xxx"
                },
                {
                    "ZoneName": "us-west-2a",
                    "SubnetId": "subnet-2yyy"
                }
            ]
        }
    ]
}
```