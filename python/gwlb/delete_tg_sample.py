#! /usr/bin/env python3

"""
Purpose:

Following sample shows you how to delete target group using Python (Boto3)
Library.
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


def main():
    """
    Deletes Target Group:

    Accepts:
    --tg_arn: ARN of Target Group to be deleted

    Usage:
    python delete_tg_sample.py \
    --tg_arn arn:aws:elasticloadbalancing:us-west-2:xxxxxxxxxxxx:targetgroup/boto3-gwlb1-tg1/002138d5900763b08b
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--tg_arn', required=True,
                        help='specify Target Group ARN', type=str)
    args = parser.parse_args()
    ############################
    # Define script variables:
    ############################
    tg_arn = args.tg_arn
    ############################
    delete_tg(tg_arn)


if __name__ == '__main__':
    main()
