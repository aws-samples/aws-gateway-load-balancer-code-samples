* Following example show how to modify VPC Endpoint Service Permissions using Python (Boto3) Library.

```python
#! /usr/bin/env python3

import argparse
import boto3
import logging
from botocore.exceptions import ClientError

# create required boto3 clients and resources:
ec2 = boto3.client('ec2')


def modify_vpce_service_permissions(service_id, principal_arns, add_remove):
    """
    Modifies the permissions for your VPC endpoint service.
    You can add or remove permissions for service consumers (IAM users,
    IAM roles, and AWS accounts) to connect to your endpoint service.
    If you grant permissions to all principals, the service is public.
    Any users who know the name of a public service can send a request
    to attach an endpoint. If the service does not require manual approval,
    attachments are automatically approved.

    Accepts
    - service_id: Service id.
    - principal_arns (list of str): List of principal arns ['iam_user1_arn']
    - add_remove (str): Add or remove specified principal. 'add'|'remove'

    Usage:
    - modify_vpce_service_permissions('service1', ['principal_arn'], 'add',
    True, db_dict)
    - modify_vpce_service_permissions('vpce-svc-xxxx', ['principal_arn'],
    'add')
    """
    logging.info(f"Removing {principal_arns} from VPCE Service: {service_id}")
    try:
        if add_remove == 'add':
            response = ec2.modify_vpc_endpoint_service_permissions(
                ServiceId=service_id,
                AddAllowedPrincipals=principal_arns
            )
        elif add_remove == 'remove':
            response = ec2.modify_vpc_endpoint_service_permissions(
                ServiceId=service_id,
                RemoveAllowedPrincipals=principal_arns
            )
        return response
    except ClientError as e:
        logging.error(e)
        return None


def main():
    """
    Adds/Removes AWS Principal to a VPC Endpoint Service (VPC-E Service)

    Accepts: service_id, principal_arns, add_remove
    --service_id: VPC-E Service id
    --principal_arns: iam_user1_arn
    --remove: remove arns

    Usage:
    ./modify_vpc_endpoint_service_permissions.py \
    --service_id vpce-svc-xxxx \
    --principal_arns iam-user1-arn \
    --add_remove add

    To remove:
    ./modify_vpc_endpoint_service_permissions.py \
    --service_id vpce-svc-xxxx \
    --principal_arns iam-user1-arn \
    --remove
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--service_id', required=True,
                        help='specify target group name', type=str)
    parser.add_argument('--principal_arns', nargs='+', required=True,
                        help='specify gwlb arns')
    parser.add_argument('--add_remove', required=True,
                        help='add or remove principals', type=str)

    args = parser.parse_args()

    ############################
    # Define script variables:
    ############################
    service_id = args.service_id
    principal_arns = args.principal_arns
    add_remove = args.add_remove
    #############################

    # VPC-E Service:
    service1 = modify_vpce_service_permissions(service_id, principal_arns,
                                               add_remove)


if __name__ == '__main__':
    main()
```