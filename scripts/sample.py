# BugyoCloudClient usage sample
#
#
import logging
from argparse import ArgumentParser

import bugyocloudclient as bcc

logging.basicConfig(level=logging.DEBUG)


def create_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument('tenant_code', nargs=1, help='Tenant code')
    parser.add_argument('login_id', nargs=1, help='Login ID')
    parser.add_argument('password', nargs=1, help='Password')
    return parser


def create_client(tenant_code: str) -> bcc.BugyoCloudClient:
    return bcc.BugyoCloudClient(tenant_code)


def create_login_task(login_id: str, password: str) -> bcc.LoginTask:
    auth_info = bcc.AuthInfo(login_id, password)
    return bcc.LoginTask(auth_info)


def create_punch_task(clock_type: bcc.ClockType) -> bcc.PunchTask:
    punch_info = bcc.PunchInfo()
    punch_info.clock_type = clock_type
    punch_info.latitude = 35.6812
    punch_info.longitude = 139.7742
    return bcc.PunchTask(punch_info)


def main():
    parser = create_parser()
    args = parser.parse_args()
    tenant_code = args.tenant_code.pop()
    login_id = args.login_id.pop()
    password = args.password.pop()

    # Create Bugyo Cloud Client
    client = create_client(tenant_code)

    # Create tasks
    login_task = create_login_task(login_id, password)
    punch_task = create_punch_task(bcc.ClockType.clock_in)

    # Execute login task
    client.exec(login_task)

    # Execute another task
    client.exec(punch_task)


if __name__ == '__main__':
    main()
