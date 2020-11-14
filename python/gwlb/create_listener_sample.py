#! /usr/bin/env python3

"""
Purpose:

Following sample shows you how to create listener using Python (Boto3) Library.

For Gateway Load Balancer (GWLB), listener doesn't support protocol and port
attribute.
"""

import argparse
import boto3
import logging
from botocore.exceptions import ClientError

# create required boto3 clients and resources:
elbv2 = boto3.client('elbv2')


def create_fwd_listener(gwlb_arn, tg_arn):
    """
    Creates a listener for the specified GWLB.

    Accepts:
    - gwlb_arn: Load balancer ARN
    - tg_arn: Target group ARN

    Usage:
    - create_fwd_listener('gwlb-arn', 'tg-arn')
    """
    try:
        response = elbv2.create_listener(
            LoadBalancerArn=gwlb_arn,
            DefaultActions=[
                {
                    'Type': 'forward',
                    'TargetGroupArn': tg_arn,
                }
            ]
        )
        listener_arn = response['Listeners'][0]['ListenerArn']
        return response, listener_arn
    except ClientError as e:
        logging.error(e)
        return None


def main():
    """
    Creates Listener:

    Accepts:
    --gwlb_arn: GWLB ARN
    --tg_arn: TG ARN    

    Usage:
    python create_listener_sample.py \
    --gwlb_arn <gwlb_arn> \
    --tg_arn <tg_arm>     
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--gwlb_arn', required=True,
                        help='specify gateway load balancer ARN', type=str)
    parser.add_argument('--tg_arn', required=True,
                        help='specify target group ARN', type=str)                        

    args = parser.parse_args()
    ############################
    # Define script variables:
    ############################
    gwlb_arn = args.gwlb_arn
    tg_arn = args.tg_arn
    #############################
    # Listener:
    listener1 = create_fwd_listener(gwlb_arn, tg_arn)
    print(f"LISTENER ARN: {listener1[1]}")


if __name__ == '__main__':
    main()