from bugyocloudclient.endpoints.timeclock import TimeClock
from bugyocloudclient.endpoints.punchmarkpage import PunchmarkPage
from bugyocloudclient.core import BugyoCloudClient
from bugyocloudclient.tasks.punchtask import PunchTask
from bugyocloudclient.models.punchinfo import PunchInfo


class TestPunchTask(object):
    def test_create_instance(self, mocker):
        """
        インスタンス生成します。
        """
        # Given
        punch_info = mocker.Mock(PunchInfo)

        # When
        instance = PunchTask(punch_info)

        # Then
        assert isinstance(instance, PunchTask)

    def test_call(self, mocker):
        # Given
        punch_info = PunchInfo()
        instance = PunchTask(punch_info)
        client = mocker.Mock(BugyoCloudClient)
        punchmark_page = mocker.Mock(PunchmarkPage)
        time_clock = mocker.Mock(TimeClock)
        token = 'one token'

        mocker.patch('bugyocloudclient.tasks.punchtask.PunchmarkPage',
                     return_value=punchmark_page)
        mocker.patch('bugyocloudclient.tasks.punchtask.TimeClock',
                     return_value=time_clock)

        punchmark_page.call.return_value = token

        # モック呼び出し順をテストするため
        manager = mocker.Mock()
        manager.attach_mock(punchmark_page, 'punchmark_page')
        manager.attach_mock(time_clock, 'time_clock')

        # When
        instance.execute(client)

        # Then
        expected_calls = [
            mocker.call.punchmark_page.call(client),
            mocker.call.time_clock.call(client, token, punch_info),
        ]
        assert manager.mock_calls == expected_calls
