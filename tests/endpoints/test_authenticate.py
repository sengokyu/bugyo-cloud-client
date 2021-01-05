from bugyocloudclient.core import BugyoCloudClient
from bugyocloudclient.endpoints.authenticate import Authenticate
from bugyocloudclient.models.authinfo import AuthInfo
from bugyocloudclient.models.clientparam import ClientParam
from requests.models import Response


class TestAuthenticate:
    def test_create_instance(self, mocker):
        # Given

        # When
        instance = Authenticate()

        # Then
        assert isinstance(instance, Authenticate)

    def test_call(self, mocker):
        """ 認証情報をPOSTしてRedirectURLを返します"""
        # Given
        instance = Authenticate()
        client = mocker.Mock(spec=BugyoCloudClient)
        token = 'token value'
        resp = mocker.Mock(Response)
        login_id = 'id'
        password = 'pass'
        auth_info = AuthInfo(login_id, password)
        redirect_url = 'https://example.com/redirect'
        tenant_code = 'ttt'
        param = ClientParam(tenant_code)

        resp.json.return_value = {
            'RedirectURL': redirect_url
        }
        client.session.post.return_value = resp
        client.param = param

        # When
        actual = instance.call(client, token, auth_info)

        # Then
        assert actual == redirect_url

        client.session.post.assert_called_once()
        expected_args = ()
        expected_kwargs = {
            'url': 'https://id.obc.jp/{0}/login/login/?Length=5'.format(
                tenant_code),
            'data': {
                '__RequestVerificationToken': token,
                'OBCID': login_id,
                'Password': password,
                'btnLogin': None,
                'Password_d1': None,
                'Password_d2': None,
                'Password_d3': None,
                'X-Requested-With': 'XMLHttpRequest',
            },
        }
        args, kwargs = client.session.post.call_args
        assert args == expected_args
        assert kwargs == expected_kwargs
