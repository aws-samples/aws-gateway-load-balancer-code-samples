* Following example show how to create listener using Python (Boto3) Library.

```python
#! /usr/bin/env python3

import argparse
import boto3
import logging
from botocore.exceptions import ClientError

# create required boto3 clients and resources:
elbv2 = boto3.client('elbv2')


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


def main():
    """
    Creates Listener:

    Accepts:
    --tg_arn: TG ARN
    --gwlb_arn: GWLB ARN

    Usage:
    ./create_gwlb_tg_listener.py \
    --tg_arn <tg_arm> \
    --gwlb_arn <gwlb_arn>
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--tg_arn', required=True,
                        help='specify target group ARN', type=str)
    parser.add_argument('--gwlb_arn', required=True,
                        help='specify gateway load balancer ARN', type=str)

    args = parser.parse_args()
    ############################
    # Define script variables:
    ############################
    tg_arn = args.tg_arn
    gwlb_arn = args.gwlb_arn

    #############################
    # Listener:
    listener1 = create_fwd_listener(gwlb_arn, tg_arn)
    print(f"LISTENER ARN: {listener1[1]}")


if __name__ == '__main__':
    main()
```
