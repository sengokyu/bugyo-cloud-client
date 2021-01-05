from bugyocloudclient.core import BugyoCloudClient
from bugyocloudclient.endpoints.timeclock import TimeClock
from bugyocloudclient.models.clientparam import ClientParam
from bugyocloudclient.models.punchinfo import ClockType, PunchInfo
from requests import Response


class TestTimeClock(object):
    def test_create_instance(self):
        """
        インスタンス生成します。
        """
        # When
        instance = TimeClock()

        # Then
        assert isinstance(instance, TimeClock)

    def test_call(self, mocker):
        """
        打刻情報をPOSTします。
        """
        # Given
        instance = TimeClock()
        tenant_code = 'a tenant'
        user_code = 'a user'
        token = 'one token'
        client = mocker.Mock(BugyoCloudClient)
        response = mocker.Mock(Response)
        param = ClientParam(tenant_code)
        punch_info = PunchInfo()

        param.user_code = user_code
        client.param = param
        punch_info.clock_type = ClockType.clock_in

        response.status_code = 200
        client.session.post.return_value = response

        # When
        instance.call(client, token, punch_info)

        # Then
        client.session.post.assert_called_once()

        expected_args = ()
        expected_kwargs = {
            'url': 'https://hromssp.obc.jp/{0}/{1}/TimeClock/InsertReadDateTime/'.format(tenant_code, user_code),
            'headers': {
                '__RequestVerificationToken': token,
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'https://hromssp.obc.jp/{0}/{1}/timeclock/punchmark/'.format(tenant_code, user_code),
            },
            'data': {
                'ClockType': 'ClockIn',
                'LaborSystemID': '0',
                'LaborSystemCode': '',
                'LaborSystemName': '',
                'PositionLatitude': 0,
                'PositionLongitude': 0,
                'PositionAccuracy': '0',
            },
            'allow_redirects': False,
        }
        args, kwargs = client.session.post.call_args
        assert args == expected_args
        assert kwargs == expected_kwargs
