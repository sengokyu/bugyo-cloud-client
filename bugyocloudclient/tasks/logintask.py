from ..authinfo import AuthInfo
from ..core import BugyoCloudClient
from ..endpoints.authenticate import Authenticate
from ..endpoints.checkauthenticationmethod import CheckAuthenticationMethod
from ..endpoints.loginpage import LoginPage
from ..tasks.abtask import ABTask
from ..utils.loginpageparser import LoginPageParser


class LoginTask(ABTask):
    """ ログインします """

    def __init__(self, auth_info: AuthInfo):
        self.__top_url = ''
        self.__auth_info = auth_info

    @property
    def top_url(self) -> str:
        return self.__top_url

    def execute(self, client: BugyoCloudClient) -> None:
        login_page = LoginPage(client, LoginPageParser())
        login_page.call()

        check_auth_method = CheckAuthenticationMethod(client)
        check_auth_method.call(self.__auth_info)

        authenticate = Authenticate(client, login_page)
        authenticate.call(self.__auth_info)

        self.__top_url = authenticate.top_url
