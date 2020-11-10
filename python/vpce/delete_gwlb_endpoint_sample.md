* Following example show how to delete Gateway Load Balancer Endpoint using Python (Boto3) Library.

```python
#! /usr/bin/env python3

import argparse
import boto3
import logging
from botocore.exceptions import ClientError

# create required boto3 clients and resources:
ec2 = boto3.client('ec2')


def delete_gwlbe(gwlbe_ids):
    """
    Deletes VPC Endpoint (GWLB-E).

    Accepts:
    - gwlbe_ids (list of str): ['vpce-svc-xxxx', 'vpce-svc-yyyy']

    Usage:
    - delete_gwlbe(['vpce-xxxx', 'vpce-yyyy'])
    """
    logging.info(f"Deleting VPC Endpoint Service:")
    try:
        response = ec2.delete_vpc_endpoints(
            VpcEndpointIds=gwlbe_ids
        )
        return response
    except ClientError as e:
        logging.error(e)
        return None


def main():
    """
    Deletes VPC Endpoint (GWLB-E)

    Accepts:
    --gwlbe_ids: GWLB-E ids

    Usage:
    ./create_gwlb_tg_listener.py \
    --gwlbe_ids vpce-0916122bdbd1ca93e
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--gwlbe_ids', nargs='+', required=True,
                        help='specify gwlbe ids')

    args = parser.parse_args()

    ############################
    # Define script variables:
    ############################
    gwlbe_ids = args.gwlbe_ids
    #############################

    # GWLB-E:
    gwlbe1 = delete_gwlbe(gwlbe_ids)
    print(gwlbe1)


if __name__ == '__main__':
    main()
```