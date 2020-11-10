* Following example show how to create Gateway Load Balancer using Python (Boto3) Library.

```python
#! /usr/bin/env python3

import argparse
import boto3
import logging
from botocore.exceptions import ClientError

# create required boto3 clients and resources:
elbv2 = boto3.client('elbv2')

def create_gwlb(gwlb_name, subnet_id_list):
    """
    Creates a Gateway Load Balancer and resturns response and ARN

    Accepts:
    - gwlb_name: Gateway Load Balancer name.
    - subnet_id_list: List of subnet id to be assigned to GWLB

    Usage:
    - create_gwlb('gwlb123', ['subnet-123'])
    """
    logging.info(f"Creating gateway load balancer: {gwlb_name}")
    waiter = elbv2.get_waiter('load_balancer_available')
    try:
        response = elbv2.create_load_balancer(
            Name=gwlb_name,
            Subnets=subnet_id_list,
            Tags=[{'Key': 'Name', 'Value': gwlb_name}],
            Type='gateway'
        )
        gwlb_arn = response['LoadBalancers'][0]['LoadBalancerArn']
        logging.info(f"Waiting for GWLB's state to change to available")
        waiter.wait(
            LoadBalancerArns=[gwlb_arn],
            WaiterConfig={
                'Delay': 15,
                'MaxAttempts': 40
            }
        )
        return response, gwlb_arn
    except ClientError as e:
        logging.error(e)
        return None


def main():
    """
    Creates Gateway Load Balancer (GWLB)

    Accepts:
    --gwlb_name: GWLB name
    --subnet_ids: Subnet ids to be assocated with GWLB

    Usage:
    ./create_gwlb.py --gwlb_name boto3-gwlb \
    --subnet_ids 'subnet-0348ec3f4869e2a1f' 'subnet-04132654a0e466491'
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--gwlb_name', required=True,
                        help='specify gateway load balancer name', type=str)
    parser.add_argument('--subnet_ids', nargs='+', required=True,
                        help='specify subnet ids')

    args = parser.parse_args()
    ############################
    # Define script variables:
    ############################
    gwlb_name = args.gwlb_name
    subnet_ids = args.subnet_ids
    #############################
    # GWLB:
    gwlb1 = create_gwlb(gwlb_name, subnet_ids)
    gwlb1_arn = gwlb1[0]['LoadBalancers'][0]['LoadBalancerArn']
    print(f"GWLB ARN: {gwlb1_arn}")

if __name__ == '__main__':
    main()
```
