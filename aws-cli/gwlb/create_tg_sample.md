Following example shows how to create target group for Gateway Load Balancer (GWLB) using [elbv2 create-target-group](https://docs.aws.amazon.com/cli/latest/reference/elbv2/create-target-group.html) command using AWS CLI version 1. Replace the parameter values inside '< >' with appropriate values. 

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

* As shown above, by default target group gets created with healthcheck configured for protocol: TCP, port:80. If you don't have anything configured on appliances to listen on TCP:80, your health checks will fail and instances will be marked unhealthy. For more details, refer to [Target Groups for your Gateway Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/target-groups.html)

* In the example below, for healthcheck, we overide the port and use HTTP, port 80. Appliances should be listening and respodning to HTTP, or else healthcheck will fail. Replace the parameter values inside '< >' with appropriate values. 

* Command:

```bash
aws elbv2 create-target-group \
    --protocol GENEVE \
    --port 6081 \
    --health-check-protocol HTTP \
    --health-check-port 80 \
    --name <gwlb1-tg1> \
    --vpc-id <appliance-vpc-id> \
    --target-type instance
```

* Output:

```bash
{
    "TargetGroups": [
        {
            "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:xxxxxxxxxxxx:targetgroup/test-tg1/0074d92ab52ead8356",
            "TargetGroupName": "test-tg1",
            "Protocol": "GENEVE",
            "Port": 6081,
            "VpcId": "vpc-0f3a17d40aeade194",
            "HealthCheckProtocol": "HTTP",
            "HealthCheckPort": "80",
            "HealthCheckEnabled": true,
            "HealthCheckIntervalSeconds": 10,
            "HealthCheckTimeoutSeconds": 5,
            "HealthyThresholdCount": 3,
            "UnhealthyThresholdCount": 3,
            "HealthCheckPath": "/",
            "Matcher": {
                "HttpCode": "200-399"
            },
            "TargetType": "instance"
        }
    ]
}
```