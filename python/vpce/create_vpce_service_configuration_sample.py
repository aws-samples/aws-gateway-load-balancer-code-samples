#! /usr/bin/env python3

"""
Purpose:

Following sample shows you how to create VPC Endpoint Service using Gateway
Load Balancer (GWLB) ARN using Python (Boto3) Library.
"""

import argparse
import boto3
import logging
from botocore.exceptions import ClientError

# create required boto3 clients and resources:
ec2 = boto3.client('ec2')


def create_vpce_service(gwlb_arns, acceptance=True):
    """
    Creates VPC Endpoint Service.

    Accepts:
    - gwlb_arns : ['gwlb1_arn']
    - acceptance (bool): True|False. Default is True

    Usage:
    - create_vpce_service(['gwlb1_arn'], True)
    """
    logging.info("Creating VPC Endpoint Service:")
    try:
        response = ec2.create_vpc_endpoint_service_configuration(
            AcceptanceRequired=acceptance,
            GatewayLoadBalancerArns=gwlb_arns,
        )
        service_id = response['ServiceConfiguration']['ServiceId']
        service_name = response['ServiceConfiguration']['ServiceName']
        return response, service_id, service_name
    except ClientError as e:
        logging.error(e)
        return None


def main():
    """
    Creates VPC Endpoint Service (VPC-E Service)

    Accepts:
    --gwlb_arns: gwlb1_arn

    Usage:
    Acceptance not required:
    python create_vpce_service_configuration_sample.py \
    --gwlb_arn gwlb1-arn
    --no_acceptance

    Acceptance required:
    python create_vpce_service_configuration_sample.py \
    --gwlb_arn gwlb1-arn
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--gwlb_arns', nargs='+', required=True,
                        help='specify gwlb arns')
    parser.add_argument('--no_acceptance', action='store_false', help='Specify'
                        ' whether to accept or not. If you want to use False,'
                        ' specify --no_acceptance with no value. If you want to'
                        ' use True, do not specity the --no_acceptance at all')

    args = parser.parse_args()

    ############################
    # Define script variables:
    ############################
    gwlb_arns = args.gwlb_arns
    no_acceptance = args.no_acceptance
    #############################

    # VPC-E Service:
    service1 = create_vpce_service(gwlb_arns, no_acceptance)
    print(f"SERVICE1 ID: {service1[1]}")
    print(f"SERVICE1 NAME: {service1[2]}")


if __name__ == '__main__':
    main()
