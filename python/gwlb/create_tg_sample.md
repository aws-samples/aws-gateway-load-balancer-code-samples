* Following example show how to create target group using Python (Boto3) Library.

```python
#! /usr/bin/env python3

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
    ./create_gwlb_tg_listener.py \
    --tg_name provider-gwlb-tg1 \
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
        'vpc_id': vpc_id,
        'type': 'instance'
    }
    #############################
    # Target Group:
    tg1 = create_tg(**tg1_args)
    print(f"TG ARN: {tg1[1]}")


if __name__ == '__main__':
    main()
```    
