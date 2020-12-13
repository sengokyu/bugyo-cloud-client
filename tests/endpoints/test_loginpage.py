import pytest

from bugyocloudclient.bugyocloudclient import BugyoCloudClient
from bugyocloudclient.endpoints.loginpage import LoginPage


class TestLoginPage():
    def test_create_instance(self, mocker) -> None:
        # Given
        loginPageParser = mocker.Mock()
        mocker.patch.object(utils.loginpageparser, 'LoginPageParser')
        client = mocker.Mock()
        client.login_url = 'https://example.com/login'
        client.prepare_request = mocker.Mock()
        client.send = mocker.Mock()

        # prepped = mocker.Mock()
        # mocker.patch.object(bugyocloudclient.BugyoCloudClient, 'prepare_request',

        # When
        instance = LoginPage(client)

        # Then
        client.prepare_request.assert_called_once()
        client.send.assert_called_once()
