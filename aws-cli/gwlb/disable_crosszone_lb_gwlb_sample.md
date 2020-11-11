Following example shows how to enbable cross-zone load balancing on Gateway Load Balancer using [elbv2 modify-load-balancer-attributes](https://docs.aws.amazon.com/cli/latest/reference/elbv2/modify-load-balancer-attributes.html) command using AWS CLI version 1. Replace the parameter values inside '< >' with appropriate values.

* Command:

```bash
aws --profile <profile1> elbv2 modify-load-balancer-attributes \
--load-balancer-arn <gwlb-arn> \
--attributes Key=load_balancing.cross_zone.enabled,Value=false
```

* Output:

```bash
{
    "Attributes": [
        {
            "Key": "deletion_protection.enabled",
            "Value": "false"
        },
        {
            "Key": "load_balancing.cross_zone.enabled",
            "Value": "false"
        }
    ]
}
```