* Following example show how to delete target group and Gateway Load Balancer using Python (Boto3) Library.

```python
#! /usr/bin/env python3

import argparse
import boto3
import logging
from botocore.exceptions import ClientError

# create required boto3 clients and resources:
elbv2 = boto3.client('elbv2')


def delete_tg(tg_arn):
    """
    Deletes target group and returns response

    Accepts:
    - tg_arn: Target group ARN. Not required if retrieving from DynamoDB

    Usage:
    - delete_tg('arn:aws:elasticloadbalancing:xxxxx')
    """
    logging.info(f"Deleting target group:")
    try:
        response = elbv2.delete_target_group(TargetGroupArn=tg_arn)
        return response
    except ClientError as e:
        logging.error(e)
        return None


def delete_gwlb(gwlb_arn):
    """
    Deletes specified GWLB and its attached listeners.

    Accepts:
    - gwlb_arn: GWLB ARN.

    Usage:
    - delete_elb('gwlb-arn')
    """
    logging.info(f"Deleting GWLB:")
    waiter = elbv2.get_waiter('load_balancers_deleted')
    try:
        response = elbv2.delete_load_balancer(LoadBalancerArn=gwlb_arn)
        logging.info(f"Waiting for GWLB's state to change to deleted")
        waiter.wait(
            LoadBalancerArns=[gwlb_arn],
            WaiterConfig={
                'Delay': 15,
                'MaxAttempts': 40
            }
        )
        return response
    except ClientError as e:
        logging.error(e)
        return None


def main():
    """
    Delete GWLB and associated Target Group and Listener:

    Accepts:
    --tg_arn: ARN of Target Group to be deleted
    --gwlb_arn: ARN of Gateway Load Balancer to be deleted

    Usage:
    ./delete_gwlb_tg.py \
    --tg_arn arn:aws:elasticloadbalancing:sa-east-1:xxxxxxxxxxxx:targetgroup/gwlb-tg1/002138d5900763b08b \
    --gwlb_arn arn:aws:elasticloadbalancing:sa-east-1:xxxxxxxxxxxx:loadbalancer/gwlb/provider-gwlb1/8b4c4f9ff8dfc05f
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--tg_arn', required=True,
                        help='specify Target Group ARN', type=str)
    parser.add_argument('--gwlb_arn', required=True,
                        help='specify Gateway Load Balancer ARN', type=str)
    args = parser.parse_args()
    ############################
    # Define script variables:
    ############################
    tg_arn = args.tg_arn
    gwlb_arn = args.gwlb_arn
    ############################
    delete_gwlb(gwlb_arn)
    delete_tg(tg_arn)


if __name__ == '__main__':
    main()
```