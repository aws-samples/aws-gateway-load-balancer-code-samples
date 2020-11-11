Following example shows how to create target group for Gateway Load Balancer using [elbv2 create-target-group](https://docs.aws.amazon.com/cli/latest/reference/elbv2/create-target-group.html) command using AWS CLI version 1. Replace the parameter values inside '< >' with appropriate values

* Command:

```bash
aws elbv2 create-target-group \
    --protocol GENEVE \
    --port 6081 \
    --name <gwlb1-tg1> \
    --vpc-id <appliance-vpc-id> \
    --target-type instance
```

* Output:

```bash
{
    "TargetGroups": [
        {
            "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:xxxxxxxxxxxx:targetgroup/cli-gwlb1-tg1/00acf64b4f3c5bdee6",
            "TargetGroupName": "cli-gwlb1-tg1",
            "Protocol": "GENEVE",
            "Port": 6081,
            "VpcId": "vpc-xxxx",
            "HealthCheckProtocol": "TCP",
            "HealthCheckPort": "80",
            "HealthCheckEnabled": true,
            "HealthCheckIntervalSeconds": 10,
            "HealthCheckTimeoutSeconds": 5,
            "HealthyThresholdCount": 3,
            "UnhealthyThresholdCount": 3,
            "TargetType": "instance"
        }
    ]
}
```