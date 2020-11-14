#! /usr/bin/env python3

"""
Purpose:

Following sample shows you how to delete VPC Endpoint Service using Python
(Boto3) Library.
"""

import argparse
import boto3
import logging
from botocore.exceptions import ClientError

# create required boto3 clients and resources:
ec2 = boto3.client('ec2')


def delete_vpce_service(service_ids):
    """
    Deletes VPC Endpoint Service.

    Accepts:
    - service_id (str): ['vpce-svc-xxxx', 'vpce-svc-yyyy']

    Usage:
    - delete_vpce_service(['vpce-svc-xxxx', 'vpce-svc-yyyy'])
    """
    logging.info("Creating VPC Endpoint Service:")
    try:
        response = ec2.delete_vpc_endpoint_service_configurations(
            ServiceIds=service_ids
        )
        return response
    except ClientError as e:
        logging.error(e)
        return None


def main():
    """
    Deletes VPC Endpoint Service (VPC-E Service)

    Accepts:
    --service_ids: VPC-E Service id

    Usage:
    python delete_vpce_service_sample.py \
    --service_ids vpce-svc-xxxx vpce-svc-yyyy
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--service_ids', nargs='+', required=True,
                        help='specify service ids')

    args = parser.parse_args()

    ############################
    # Define script variables:
    ############################
    service_ids = args.service_ids
    #############################

    # VPC-E Service:
    service1 = delete_vpce_service(service_ids)


if __name__ == '__main__':
    main()
