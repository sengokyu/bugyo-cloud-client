from ..bugyocloudclient import BugyoCloudClient
from ..utils.baserequest import BaseRequest
from .loginpageparser import LoginPageParser


class LoginPage:
    """ ログインページ読み込みます """

    def __init__(self, client: BugyoCloudClient) -> None:
        self.client = client

        parser = LoginPageParser(self.__load())

        self.action = parser.action
        self.token_value = parser.token_value

    def __load(self) -> str:
        req = BaseRequest('GET', self.client.login_url)
        prepped = self.client.prepare_request(req)

        resp = self.client.send(prepped)
        resp.raise_for_status()

        return resp.content.decode(BugyoCloudClient.ENCODING)
