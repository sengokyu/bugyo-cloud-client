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

        resp.json = {
            'RedirectURL': redirect_url
        }
        client.session.post.return_value = resp
        client.param = param

        # When
        actual = instance.call(client, token, auth_info)

        # Then
        assert actual == redirect_url

        client.session.post.assert_called_once()

        args, kwargs = client.session.post.call_args

        assert kwargs['url'] == 'https://id.obc.jp/{0}/login/login/?Length=5'.format(
            tenant_code)
        assert kwargs['data']['__RequestVerificationToken'] == token
        assert kwargs['data']['OBCID'] == login_id
        assert kwargs['data']['Password'] == password
