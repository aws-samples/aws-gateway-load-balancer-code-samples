* Following example show how to create VPC Endpoint Service using Gateway Load Balancer ARN using Python (Boto3) Library.

```python
#! /usr/bin/env python3

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
    - gwlb_arns : ['gwlb1_arn' 'gwlb2_arn']
    - acceptance (bool): True|False. Default is True

    Usage:
    - create_vpce_service(['gwlb1_arn'], True)
    """
    logging.info(f"Creating VPC Endpoint Service:")
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
    ./create_vpc_endpoint_service.py \
    --gwlb_arn gwlb1-arn
    --accept

    Acceptance required:
    ./create_vpc_endpoint_service.py \
    --gwlb_arn gwlb1-arn
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--gwlb_arns', nargs='+', required=True,
                        help='specify gwlb arns')
    parser.add_argument('--accept', action='store_false', help='Specify'
                        ' whether to accept or not. If you want to accept'
                        ' (False) specify --accept with no value. '
                        ' If you want do not want to accept (True),'
                        ' do not specify the --accept arg')

    args = parser.parse_args()

    ############################
    # Define script variables:
    ############################
    gwlb_arns = args.gwlb_arns
    accept = args.accept
    #############################

    # VPC-E Service:
    service1 = create_vpce_service(gwlb_arns, accept)
    print(f"SERVICE1 ID: {service1[1]}")
    print(f"SERVICE1 NAME: {service1[2]}")


if __name__ == '__main__':
    main()
```