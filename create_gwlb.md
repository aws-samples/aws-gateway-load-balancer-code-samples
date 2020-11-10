* Following example shows how to create Gateway Load Balancer using
[create-load-balancer](https://docs.aws.amazon.com/cli/latest/reference/elbv2/create-load-balancer.html) command. Replace the parameter values inside '< >' with your own.

<pre><code>
aws --profile <em style="color: green;">profile1</em> elbv2 create-load-balancer \
--type gateway \
--subnets <i>subnet-xxxxxxxx</i> <i>subnet-yyyyyyyy</i> \
--name <i>gwlb1</i>
</code></pre>
