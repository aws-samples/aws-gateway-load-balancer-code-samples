* Following example show how to modify VPC Endpoint Service Configuration using Python (Boto3) Library.

```python
#! /usr/bin/env python3

import argparse
import boto3
import logging
from botocore.exceptions import ClientError

# create required boto3 clients and resources:
ec2 = boto3.client('ec2')


def modify_vpce_service_acceptance(service_id, accept=True):
    """
    Allows to either accept (True) or reject(False) requests to
    create an endpoint to the service.

    Accepts
    - service_id: Service id.
    - accept (bool): True|False: Default is True (accept)

    Usage:
    - modify_vpce_service_acceptance('service1', True, True, db_dict)
    - modify_vpce_service_acceptance('service-xxxx', False)
    """
    logging.info(f"Changing AcceptaneRequired to {accept} for"
                 f" VPCE Service:")
    try:
        response = ec2.modify_vpc_endpoint_service_configuration(
            ServiceId=service_id,
            AcceptanceRequired=accept
        )
        return response
    except ClientError as e:
        logging.error(e)
        return None


def main():
    """
    Creates VPC Endpoint Service (VPC-E Service)

    Accepts:
    --service_id: vpce-svc-xxxx
    --no_accept

    Usage: To not accept:
    ./create_gwlb_tg_listener.py \
    --service_id vpce-svc-xxxx \
    --no-accept
    Usage: To accept:
    ./create_gwlb_tg_listener.py \
    --service_id vpce-svc-xxxx
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--service_id', required=True,
                        help='specify service id', type=str)
    parser.add_argument('--no_accept', action='store_false', help='Specify'
                        ' whether to accept or not. If you want to use False,'
                        ' specify --no_accept with no value. If you want to'
                        ' use True, do not specity the --no_accept at all')

    args = parser.parse_args()

    ############################
    # Define script variables:
    ############################
    service_id = args.service_id
    no_accept = args.no_accept
    #############################

    # VPC-E Service:
    service1 = modify_vpce_service_acceptance(service_id, no_accept)


if __name__ == '__main__':
    main()
```
