#! /usr/bin/env python3

"""
Purpose:

Following sample shows you how to register targets to target group using
Python (Boto3) Library.
"""
##############################################################################

##############################################################################

import argparse
import boto3
import logging
from botocore.exceptions import ClientError

# create required boto3 clients and resources:
elbv2 = boto3.client('elbv2')


def register_targets(tg_arn, target_string):
    """
    Registers targets with a target group:

    Accepts:
    - target_string: The ID of the target. If the target type of the target
    group is instance , specify an instance ID.
    - tg_arn: Target group ARN. Not required if retrieving from DynamoDB

    Usage:
    - register_targets(tg_arn='arn:aws:elasticloadbalancing:xxxxx', 'i-xxxx')
    """
    logging.info(f"Registering targets with target group: {tg_arn}")
    # waiter = elb.get_waiter('target_in_service')
    try:
        response = elbv2.register_targets(
            TargetGroupArn=tg_arn,
            Targets=[
                {
                    'Id': target_string
                },
            ]
        )
        return response
    except ClientError as e:
        logging.error(e)
        return None


def main():
    """
    Creates Appliance Gateway (GWLB) and associated Target Group (TG) and
    Listener and registers target(s)

    Accepts:
    --tg_arn: TG ARN
    --target_string: target as string

    Usage:
    ./create_gwlb_tg_listener.py \
    --tg_arn <tg_arn> \
    --target_string <i-123>
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--tg_arn', required=True,
                        help='specify target group name', type=str)
    parser.add_argument('--target_id', required=True,
                        help='specify target ids')

    args = parser.parse_args()
    ############################
    # Define script variables:
    ############################
    tg_arn = args.tg_arn
    target_id = args.target_id
    #############################
    # Register Targets:
    register_targets(tg_arn, target_id)


if __name__ == '__main__':
    main()