Following example shows how to register targets with target group using [elbv2 register-targets](https://docs.aws.amazon.com/cli/latest/reference/elbv2/register-targets.html) command. Replace the parameter values inside '< >' with your own.


* Command:

```
aws elbv2 register-targets \
    --target-group-arn <gwlb1-tg1-arn> \
    --targets Id=<applaince1-id> Id=<appliance2-id>
```

* Output:

```bash
empty
```
