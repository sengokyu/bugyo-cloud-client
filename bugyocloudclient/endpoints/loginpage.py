from ..core import BugyoCloudClient
from ..utils.getrequest import GetRequest
from ..utils.loginpageparser import LoginPageParser


class LoginPage(GetRequest):
    """ ログインページのaction urlとtoken valueを読み込みます """

    def __init__(self, client: BugyoCloudClient, parser: LoginPageParser):
        self.__client = client
        self.__parser = parser
        self.__action = ''
        self.__token_value = ''
        super().__init__(self.__build_url())

    @property
    def action(self) -> str:
        return self.__action

    @property
    def token_value(self) -> str:
        return self.__token_value

    def call(self) -> None:
        content = self.__load()
        (self.__action, self.__token_value) = self.__parser.parse(content)

    def __load(self) -> str:
        prepped = self.__client.prepare_request(self)

        resp = self.__client.send(prepped)
        resp.raise_for_status()

        return resp.content.decode(BugyoCloudClient.ENCODING)

    def __build_url(self) -> str:
        return ('https://id.obc.co.jp/', self.__client.tenant_code)
