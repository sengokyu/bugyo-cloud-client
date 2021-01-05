from bugyocloudclient import BugyoCloudClient
from bugyocloudclient.endpoints.loginpage import LoginPage
from bugyocloudclient.models.clientparam import ClientParam
from requests import Response


class TestLoginPage():
    def test_create_instance(self, mocker) -> None:
        # When
        instance = LoginPage()

        # Then
        assert isinstance(instance, LoginPage)

    def test_call(self, mocker) -> None:
        """ パースしてtoken_valueがセットされる """
        # Given
        instance = LoginPage()
        client = mocker.Mock(spec=BugyoCloudClient)
        resp = mocker.Mock(Response)
        tenant_code = 'tete'
        param = ClientParam(tenant_code)
        content = '<input type="hidden" name="__RequestVerificationToken" value="one token">'

        resp.content = bytearray(content, 'utf-8')
        client.session.get.return_value = resp
        client.param = param

        # When
        actual = instance.call(client)

        # Then
        assert actual == 'one token'
        expected_url = 'https://id.obc.jp/{0}'.format(tenant_code)
        client.session.get.assert_called_once_with(expected_url)
