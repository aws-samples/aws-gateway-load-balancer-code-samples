Following example shows how to modify VPC Endpoint Service permissions using [ec2 modify-vpc-endpoint-service-permissions](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpc-endpoint-service-permissions.html) command using AWS CLI version 1. Replace the parameter values inside '< >' with appropriate values.

* Command:

```bash
aws ec2 modify-vpc-endpoint-service-permissions \
--service-id <vpce_service_id> \
--add-allowed-principals <arn:aws:iam::aws-account-id:user1>
```

* Output:

```bash
{
    "ReturnValue": true
}
```