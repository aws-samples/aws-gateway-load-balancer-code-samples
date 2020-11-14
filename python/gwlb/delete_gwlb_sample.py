#! /usr/bin/env python3

"""
Purpose:

Following sample shows you how to delete Gateway Load Balancer (GWLB) using
Python (Boto3) Library.
"""

import argparse
import boto3
import logging
from botocore.exceptions import ClientError

# create required boto3 clients and resources:
elbv2 = boto3.client('elbv2')


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
    Deletes GWLB and associated listener:

    Accepts:
    --gwlb_arn: ARN of Gateway Load Balancer to be deleted

    Usage:
    python delete_gwlb.py \
    --gwlb_arn arn:aws:elasticloadbalancing:us-west-2:xxxxxxxxxxxx:loadbalancer/gwlb/boto3-gwlb1/8b4c4f9ff8dfc05f
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--gwlb_arn', required=True,
                        help='specify Gateway Load Balancer ARN', type=str)
    args = parser.parse_args()
    ############################
    # Define script variables:
    ############################
    gwlb_arn = args.gwlb_arn
    ############################
    delete_gwlb(gwlb_arn)


if __name__ == '__main__':
    main()
