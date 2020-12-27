from bugyocloudclient.core import BugyoCloudClient
from bugyocloudclient.endpoints.authenticate import Authenticate
from bugyocloudclient.endpoints.checkauthenticationmethod import \
    CheckAuthenticationMethod
from bugyocloudclient.endpoints.loginpage import LoginPage
from bugyocloudclient.endpoints.toppage import TopPage
from bugyocloudclient.models.authinfo import AuthInfo
from bugyocloudclient.tasks.basetask import BaseTask


class LoginTask(BaseTask):
    """ ログインします """

    def __init__(self, auth_info: AuthInfo):
        self.__auth_info = auth_info

    def execute(self, client: BugyoCloudClient) -> None:
        login_page = LoginPage()
        token = login_page.call(client)

        check_auth_method = CheckAuthenticationMethod()
        check_auth_method.call(client, self.__auth_info)

        authenticate = Authenticate()
        redirect_url = authenticate.call(client, token, self.__auth_info)

        top_page = TopPage()
        user_code = top_page.call(client, redirect_url)

        client.param.user_code = user_code
