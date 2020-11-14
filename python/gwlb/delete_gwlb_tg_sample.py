#! /usr/bin/env python3

"""
Purpose:

Following sample shows you how to delete Gateway Load Balancer (GWLB) and
target group using Python (Boto3) Library.
"""

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
    logging.info("Deleting target group:")
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
    logging.info("Deleting GWLB:")
    waiter = elbv2.get_waiter('load_balancers_deleted')
    try:
        response = elbv2.delete_load_balancer(LoadBalancerArn=gwlb_arn)
        logging.info("Waiting for GWLB's state to change to deleted")
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
    --gwlb_arn: ARN of Gateway Load Balancer to be deleted
    --tg_arn: ARN of Target Group to be deleted

    Usage:
    python delete_gwlb_tg.py \
    --gwlb_arn arn:aws:elasticloadbalancing:us-west-2:xxxxxxxxxxxx:loadbalancer/gwlb/provider-gwlb1/8b4c4f9ff8dfc05f \
        --tg_arn arn:aws:elasticloadbalancing:us-west-2:xxxxxxxxxxxx:targetgroup/gwlb-tg1/002138d5900763b08b
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--gwlb_arn', required=True,
                        help='specify Gateway Load Balancer ARN', type=str)
    parser.add_argument('--tg_arn', required=True,
                        help='specify Target Group ARN', type=str)
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
