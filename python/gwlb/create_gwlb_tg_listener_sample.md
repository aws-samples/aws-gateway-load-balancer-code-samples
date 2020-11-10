* Following example show how to create Gateway Load Balancer, target group and listener using Python (Boto3) Library.

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


def register_targets(tg_arn, target_string):
    """
    Registers targets with a target group:

    Accepts:
    - target_string: The ID of the target. If the target type of the target
    group is instance , specify an instance ID.
    - tg_arn: Target group ARN. Not required if retrieving from DynamoDB

    Usage:
    - register_targets(tg_arn='arn:aws:elasticloadbalancing:xxxxx', 'i-xxxx')
    """
    logging.info(f"Registering targets with target group: {tg_arn}")
    # waiter = elb.get_waiter('target_in_service')
    try:
        response = elbv2.register_targets(
            TargetGroupArn=tg_arn,
            Targets=[
                {
                    'Id': target_string
                },
            ]
        )
        return response
    except ClientError as e:
        logging.error(e)
        return None


def main():
    """
    Creates Appliance Gateway (GWLB) and associated Target Group (TG) and
    Listener and registers target(s)

    Accepts:
    --tg_name: TG name
    --gwlb_name: GWLB name
    --vpc_id: VPC id to associate TG with
    --subnet_ids: Subnet ids to be assocated with GWLB
    --target_ids: Target ids to be registered with GWLB's TG

    Usage:
    ./create_gwlb_tg_listener.py \
    --tg_name provider-gwlb-tg1 \
    --gwlb_name provider-gwlb1 \
    --vpc_id vpc-xxxx \
    --subnet_ids subnet-xxxx subnet-yyyy \
    --target_ids i-xxxx i-yyyy
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--tg_name', required=True,
                        help='specify target group name', type=str)
    parser.add_argument('--gwlb_name', required=True,
                        help='specify gateway load balancer name', type=str)
    parser.add_argument('--vpc_id', required=True,
                        help='specify vpc id', type=str)
    parser.add_argument('--subnet_ids', nargs='+', required=True,
                        help='specify subnet ids')
    parser.add_argument('--target_ids', nargs='+', required=True,
                        help='specify target ids')

    args = parser.parse_args()
    ############################
    # Define script variables:
    ############################
    tg_name = args.tg_name
    gwlb_name = args.gwlb_name
    vpc_id = args.vpc_id
    subnet_ids = args.subnet_ids
    target_ids = args.target_ids

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
    # GWLB:
    gwlb1 = create_gwlb(gwlb_name, subnet_ids)
    print(f"GWLB ARN: {gwlb1[1]}")
    # Listener:
    listener1 = create_fwd_listener(gwlb1[1], tg1[1])
    print(f"LISTENER ARN: {listener1[1]}")
    # Register Targets:
    register_targets(tg1[1], target_ids[0])


if __name__ == '__main__':
    main()
```