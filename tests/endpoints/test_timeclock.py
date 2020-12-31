from bugyocloudclient.models.clientparam import ClientParam
from bugyocloudclient.models.punchinfo import ClockType, PunchInfo
from bugyocloudclient.core import BugyoCloudClient
from bugyocloudclient.endpoints.timeclock import TimeClock


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
        param = ClientParam(tenant_code)
        punch_info = PunchInfo()

        param.user_code = user_code
        client.param = param
        punch_info.clock_type = ClockType.clock_in

        # When
        instance.call(client, token, punch_info)

        # Then
        client.session.post.assert_called_once()

        args, kwargs = client.session.post.call_args

        assert len(args) == 0
        assert len(kwargs) == 3
        assert kwargs['url'] == 'https://hromssp.obc.jp/{0}/{1}/TimeClock/InsertReadDateTime/'.format(
            tenant_code, user_code)
        assert len(kwargs['headers']) == 1
        assert kwargs['headers']['__RequestVerificationToken'] == token
        assert len(kwargs['data']) == 7
        assert kwargs['data']['ClockType'] == 'ClockIn'
