from ..bugyocloudclient import BugyoCloudClient
from ..endpoints.authenticate import Authenticate
from ..endpoints.checkauthenticationmethod import CheckAuthenticationMethod
from ..endpoints.loginpage import LoginPage
from ..tasks.abtask import ABTask


class LoginTask(ABTask):
    """ ログインします """

    def __init__(self, client: BugyoCloudClient, password: str):
        self.client = client
        self.password = password

    def execute(self):
        login_page = LoginPage(self.client)

        check_auth_method = CheckAuthenticationMethod(self.client)
        check_auth_method.post()

        authenticate = Authenticate(self.client, login_page.action)
        authenticate.post(login_page.token_value, self.password)
