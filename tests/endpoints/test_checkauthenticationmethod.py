from bugyocloudclient.core import BugyoCloudClient
from bugyocloudclient.endpoints.checkauthenticationmethod import \
    CheckAuthenticationMethod
from bugyocloudclient.models.authinfo import AuthInfo
from bugyocloudclient.models.clientparam import ClientParam


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
        login_id = 'login'
        password = 'pass'
        auth_info = AuthInfo(login_id, password)
        tenant_code = 'tttt'
        client_param = ClientParam(tenant_code)

        client.param = client_param

        # When
        instance.call(client, auth_info)

        # Then
        client.session.post.assert_called_once()
        args, kwargs = client.session.post.call_args
        assert kwargs['url'] == 'https://id.obc.co.jp/{0}/login/CheckAuthenticationMethod'.format(
            tenant_code)
        assert kwargs['data']['OBCiD'] == login_id
