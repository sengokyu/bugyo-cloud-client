from bugyocloudclient.core import BugyoCloudClient
from bugyocloudclient.endpoints.checkauthenticationmethod import \
    CheckAuthenticationMethod
from bugyocloudclient.models.authinfo import AuthInfo
from bugyocloudclient.models.clientparam import ClientParam
from requests import Response


class TestCheckAuthenticationMethod:
    def test_create_instance(self):
        """ インスタンス生成 """
        # When
        instance = CheckAuthenticationMethod()

        # Then
        assert isinstance(instance, CheckAuthenticationMethod)

    def test_call(self, mocker):
        """ POSTするだけ """
        # Given
        instance = CheckAuthenticationMethod()
        client = mocker.Mock(spec=BugyoCloudClient)
        response = mocker.Mock(Response)
        response.status_code = 200
        token = 'verification token'
        login_id = 'login'
        password = 'pass'
        auth_info = AuthInfo(login_id, password)
        tenant_code = 'tttt'
        client_param = ClientParam(tenant_code)

        client.param = client_param
        client.session.post.return_value = response

        # When
        instance.call(client, token, auth_info)

        # Then
        client.session.post.assert_called_once()
        expected_args = ()
        expected_kwargs = {
            'url': 'https://id.obc.jp/{0}/login/CheckAuthenticationMethod'.format(tenant_code),
            'headers': {
                '__RequestVerificationToken': token,
                'X-Requested-With': 'XMLHttpRequest',
            },
            'data': {
                'OBCiD': login_id,
                'isBugyoCloud': 'false',
            },
            'allow_redirects': False
        }
        args, kwargs = client.session.post.call_args
        assert args == expected_args
        assert kwargs == expected_kwargs
