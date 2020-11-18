from unittest import TestCase
from unittest.mock import MagicMock, NonCallableMagicMock, patch

from bugyocloudclient import BugyoCloudClient
from bugyocloudclient.tasks.logintask import LoginTask


class TestLoginTask(TestCase):
    LOGIN_URL = 'https://example.com/foobar'
    CONTENT = '''\
    <form id="loginform" action="http://example.com/">
    <input name="__RequestVerificationToken" value="token value">
    </form>'''
    instance: LoginTask

    def setUp(self) -> None:
        self.instance = LoginTask()

    @patch('bugyocloudclient.BugyoCloudClient')
    def test_prepare(self, client) -> None:
        """ログインページを取得してパースします。"""
        # Given
        prepped = NonCallableMagicMock()
        resp = NonCallableMagicMock()
        resp.content = self.CONTENT.encode('utf-8')
        client.prepare_request = MagicMock(return_value=prepped)
        client.send = MagicMock(return_value=resp)

        # When
        self.instance.prepare(client)

        # Then
        client.prepare_request.assert_called_once()
        client.send.assert_called_once()
