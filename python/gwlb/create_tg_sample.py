#! /usr/bin/env python3

"""
Purpose:

Following sample shows you how to create target group using Python (Boto3)
Library.

By default target group gets created with healthcheck configured for protocol:
TCP, port:80. If you don't have anything configured on appliances to listen on
TCP:80, your health checks will fail and instances will be marked unhealthy.

In the example below, for healthcheck, we overide the port and use HTTP, port
80. Appliances should be listening and respodning to HTTP, or else healthcheck
will fail. Replace the parameter values inside '< >' with appropriate values.

For more details, refer to Target Groups for your Gateway Load Balancers
https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/target-groups.html
"""

import argparse
import boto3
import logging
from botocore.exceptions import ClientError

# create required boto3 clients and resources:
elbv2 = boto3.client('elbv2')


def create_tg(**tg_args):
    """
    Creates target group.

    Accepts:
    - tg_args: tg_args is dictionary with required key:value
    pair. You can add values to dictionary as required. Dictionary should
    strictly follow the naming convention as below:
        tg_args = {
            'name': 'tg1',
            'protocol': 'GENEVE',
            'port': 6081,
            'healthchkproto': 'HTTP',
            'healthchkport': '80',
            'healthchkpath': '/',
            'vpc_id': 'vpc-xxxx',
            'type': 'instance'
        }

    Usage:
    - create_tg(**tg_args)
    """
    logging.info(f"Creating target group: {tg_args['name']}")
    try:
        response = elbv2.create_target_group(
            Name=tg_args['name'],
            Protocol=tg_args['protocol'],
            Port=tg_args['port'],
            HealthCheckProtocol=tg_args['healthchkproto'],
            HealthCheckPort=tg_args['healthchkport'],
            HealthCheckPath=tg_args['healthchkpath'],
            VpcId=tg_args['vpc_id'],
            TargetType=tg_args['type']
        )
        tg_arn = response['TargetGroups'][0]['TargetGroupArn']
        return response, tg_arn
    except ClientError as e:
        logging.error(e)
        return None


def main():
    """
    Creates Target Group (TG)

    Accepts:
    --tg_name: TG name
    --vpc_id: VPC id to associate TG with

    Usage:
    python create_tg_sample.py \
    --tg_name boto3-gwlb1-tg1 \
    --vpc_id vpc-xxxx
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--tg_name', required=True,
                        help='specify target group name', type=str)
    parser.add_argument('--vpc_id', required=True,
                        help='specify vpc id', type=str)

    args = parser.parse_args()
    ############################
    # Define script variables:
    ############################
    tg_name = args.tg_name
    vpc_id = args.vpc_id

    tg1_args = {
        'name': tg_name,
        'protocol': 'GENEVE',
        'port': 6081,
        'healthchkproto': 'HTTP',
        'healthchkport': '80',
        'healthchkpath': '/',
        'vpc_id': vpc_id,
        'type': 'instance'
    }
    #############################
    # Target Group:
    tg1 = create_tg(**tg1_args)
    print(f"TG ARN: {tg1[1]}")


if __name__ == '__main__':
    main()