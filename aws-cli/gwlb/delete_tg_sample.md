Following example shows how to delete target group for Gateway Load Balancer using [elbv2 delete-target-group](https://docs.aws.amazon.com/cli/latest/reference/elbv2/delete-target-group.html) command. Replace the parameter values inside '< >' with appropriate values.

* Command:

```bash
aws elbv2 delete-target-group \
    --target-group-arn <gwlb1-tg1-arn>
```

* Output:

```bash
```