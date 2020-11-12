Following example shows how to modify VPC Endpoint Service configuration using [ec2 modify-vpc-endpoint-service-configuration](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpc-endpoint-service-configuration.html) command using AWS CLI version 1. Replace the parameter values inside '< >' with appropriate values.

* Command

```bash
aws ec2 modify-vpc-endpoint-service-configuration \
    --service-id <vpc-endpoint-service-id> \
    --acceptance-required
```

* Output:

```bash
{
    "Return": true
}
```