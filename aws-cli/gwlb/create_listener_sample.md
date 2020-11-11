Following example shows how to listener for Gateway Load Balancer using [elbv2 create-listener](https://docs.aws.amazon.com/cli/latest/reference/elbv2/create-listener.html) command using AWS CLI version 1. Replace the parameter values inside '< >' with appropriate values

* Command:

```bash
aws elbv2 create-listener \
    --load-balancer-arn <glwb-arn> \
    --default-actions Type=forward,TargetGroupArn=<gwlb-tg-arn>
```

* Output:

```bash
{
    "Listeners": [
        {
            "ListenerArn": "arn:aws:elasticloadbalancing:us-west-2:xxxxxxxxxxxx:listener/gwy/cli-gwlb1/dabd816b54d028e1/b1041679d4e16af2",
            "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-west-2:xxxxxxxxxxxx:loadbalancer/gwy/cli-gwlb1/dabd816b54d028e1",
            "DefaultActions": [
                {
                    "Type": "forward",
                    "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:xxxxxxxxxxxx:targetgroup/cli-gwlb1-tg1/00acf64b4f3c5bdee6",
                    "ForwardConfig": {
                        "TargetGroups": [
                            {
                                "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:xxxxxxxxxxxx:targetgroup/cli-gwlb1-tg1/00acf64b4f3c5bdee6"
                            }
                        ]
                    }
                }
            ]
        }
    ]
}
```