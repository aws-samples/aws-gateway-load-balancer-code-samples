Following example shows how to delete Gateway Load Balancer Endpoint using [ec2 delete-vpc-endpoints](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-vpc-endpoints.html) command using AWS CLI version 1. Replace the parameter values inside '< >' with appropriate values.

* Command:

```bash
aws ec2 delete-vpc-endpoints \
    --vpc-endpoint-ids <gwlb-endpoint-id>
```

* Output:

```bash
{
    "Unsuccessful": []
}
```