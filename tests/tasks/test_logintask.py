from bugyocloudclient.core import BugyoCloudClient
from bugyocloudclient.endpoints.authenticate import Authenticate
from bugyocloudclient.endpoints.checkauthenticationmethod import \
    CheckAuthenticationMethod
from bugyocloudclient.endpoints.loginpage import LoginPage
from bugyocloudclient.endpoints.toppage import TopPage
from bugyocloudclient.models.authinfo import AuthInfo
from bugyocloudclient.tasks.logintask import LoginTask


class TestLoginTask():
    def test_create_instance(self, mocker):
        # Given
        auth_info = mocker.Mock(AuthInfo)

        # When
        instance = LoginTask(auth_info)

        # Then
        assert isinstance(instance, LoginTask)

    def test_execute(self, mocker):
        """ ログイン処理を実行します。 """
        # Given
        login_page = mocker.Mock(LoginPage)
        check_auth_method = mocker.Mock(CheckAuthenticationMethod)
        authenticate = mocker.Mock(Authenticate)
        top_page = mocker.Mock(TopPage)
        auth_info = AuthInfo('login id', 'password')
        instance = LoginTask(auth_info)
        client = mocker.Mock(BugyoCloudClient)
        token = 'a token'
        redirect_url = 'https://example.com/redirect'

        mocker.patch('bugyocloudclient.tasks.logintask.LoginPage',
                     return_value=login_page)
        mocker.patch('bugyocloudclient.tasks.logintask.CheckAuthenticationMethod',
                     return_value=check_auth_method)
        mocker.patch('bugyocloudclient.tasks.logintask.Authenticate',
                     return_value=authenticate)
        mocker.patch('bugyocloudclient.tasks.logintask.TopPage',
                     return_value=top_page)
        login_page.call.return_value = token
        authenticate.call.return_value = redirect_url

        # 呼び出し順を記録する
        manager = mocker.Mock()
        manager.attach_mock(login_page, 'login_page')
        manager.attach_mock(check_auth_method, 'check_auth_method')
        manager.attach_mock(authenticate, 'authenticate')
        manager.attach_mock(top_page, 'top_page')

        # When
        instance.execute(client)

        # Then
        expected_calls = [
            mocker.call.login_page.call(client),
            mocker.call.check_auth_method.call(client, auth_info),
            mocker.call.authenticate.call(client, token, auth_info),
            mocker.call.top_page.call(client, redirect_url)
        ]
        assert manager.mock_calls == expected_calls
