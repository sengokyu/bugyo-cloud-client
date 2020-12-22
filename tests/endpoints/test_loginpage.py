from bugyocloudclient import BugyoCloudClient
from bugyocloudclient.endpoints.loginpage import LoginPage
from bugyocloudclient.utils.loginpageparser import LoginPageParser


class TestLoginPage():
    def test_create_instance(self, mocker) -> None:
        # Given
        client = mocker.Mock(spec=BugyoCloudClient)
        parser = mocker.Mock(spec=LoginPageParser)
        instance = LoginPage(client, parser)

        # Then
        assert isinstance(instance, LoginPage)

    def test_call(self, mocker) -> None:
        """ ログイン画面を取得してパース """
        # Given
        client = mocker.Mock(spec=BugyoCloudClient)
        parser = mocker.Mock(spec=LoginPageParser)
        parser.parse.return_value = ('action', 'token value')

        instance = LoginPage(client, parser)

        # When
        instance.call()

        # Then
        client.prepare_request.assert_called_once()
        client.send.assert_called_once()
        parser.parse.assert_called_once()
        assert instance.action == 'action'
        assert instance.token_value == 'token value'
