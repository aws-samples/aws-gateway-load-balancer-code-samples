* Following example shows how to create Gateway Load Balancer using
[create-load-balancer](https://docs.aws.amazon.com/cli/latest/reference/elbv2/create-load-balancer.html) command. Replace the parameter values inside '< >' with your own.

```console  
aws --profile <profile1> elbv2 create-load-balancer \
--type gateway \
--subnets <subnet-xxxxxxxx> <subnet-yyyyyyyy> \
--name <gwlb1> \
```