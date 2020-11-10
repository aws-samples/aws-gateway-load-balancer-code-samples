* Following example show how to create Gateway Load Balancer Endpoint using VPC Endpoint Service Name using Python (Boto3) Library.

```python
#! /usr/bin/env python3

import argparse
import boto3
import logging
from botocore.exceptions import ClientError

# create required boto3 clients and resources:
ec2 = boto3.client('ec2')


def create_gwlbe(service_name, vpc_id, subnet_ids):
    """
    Creates VPC Endpoint Service.

    Accepts:
    - service_name (str): VPCE Service name.
    - vpc_id : 'vpc-xxxx'
    - subnet_ids (list of str): ['subnet-xxxx'], only one subnet id for GWLBe

    Usage:
    - create_gwlbe('service_name', 'vpc-xxxx', ['subnet-xxxx']
    """
    logging.info(f"Creating VPC Endpoint of Type GatewayLoadBalancer:")
    try:
        response = ec2.create_vpc_endpoint(
            VpcEndpointType='GatewayLoadBalancer',
            VpcId=vpc_id,
            SubnetIds=subnet_ids,
            ServiceName=service_name
        )
        vpce_id = response['VpcEndpoint']['VpcEndpointId']
        vpce_id_type = response['VpcEndpoint']['VpcEndpointType']
        return response, vpce_id, vpce_id_type
    except ClientError as e:
        logging.error(e)
        return None


def main():
    """
    Creates VPC Endpoint Type GatewayLoadBalancer (GWLBE):

    Accepts:
    --service_name: VPC-E Service name
    --vpc_id: vpc id to with GWLBE is associated
    --subnet_id: list of subnet id. As of now only one subnet id supported for GWLBe

    Usage:
    ./create_vpc_endpoint.py \
    --service_name com.amazonaws.vpce.sa-east-1.vpce-svc-05c11ebdfc1b84593 \
    --vpc_id vpc-09a8e887492790aea
    --subnet_id subnet-002136cca79d6bba3
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--service_name', required=True,
                        help='specify service name', type=str)
    parser.add_argument('--vpc_id', required=True,
                        help='specify vpc id', type=str)
    parser.add_argument('--subnet_id', nargs='+', required=True,
                        help='specify subnet id')

    args = parser.parse_args()

    ############################
    # Define script variables:
    ############################
    service_name = args.service_name
    vpc_id = args.vpc_id
    subnet_id = args.subnet_id
    #############################

    # GWLBE:
    gwlbe1 = create_gwlbe(service_name, vpc_id, subnet_id)
    print(f"GWLBE1 ID: {gwlbe1[1]}")
    print(f"GWLBE1 TYPE: {gwlbe1[2]}")


if __name__ == '__main__':
    main()
```
