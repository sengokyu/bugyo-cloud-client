from unittest import TestCase
from unittest.mock import MagicMock, NonCallableMagicMock, patch

from bugyocloudclient import BugyoCloudClient
from bugyocloudclient.authinfo import AuthInfo
from bugyocloudclient.tasks.logintask import LoginTask


class TestLoginTask(TestCase):

    def setUp(self, mocker) -> None:
        self.auth_info = mocker.Mock(AuthInfo)
        self.instance = LoginTask(self.auth_info)

    # def test_prepare(self, client) -> None:
    #     """ログインページを取得してパースします。"""
    #     # Given
    #     prepped = NonCallableMagicMock()
    #     resp = NonCallableMagicMock()
    #     resp.content = self.CONTENT.encode('utf-8')
    #     client.prepare_request = MagicMock(return_value=prepped)
    #     client.send = MagicMock(return_value=resp)

    #     # When
    #     self.instance.prepare(client)

    #     # Then
    #     client.prepare_request.assert_called_once()
    #     client.send.assert_called_once()
