Following example shows how to delete VPC Endpoint Service [ec2 delete-vpc-endpoint-service-configurations](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-vpc-endpoint-service-configurations.html) command. Replace the parameter values inside '< >' with appropriate values.

* Command

```bash
aws ec2 delete-vpc-endpoint-service-configurations \
    --service-ids <vpc-endpoint-service-id>
```

* Output:

```bash
{
    "Unsuccessful": []
}
```
