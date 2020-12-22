from bugyocloudclient.authinfo import AuthInfo
from requests.models import Response

from ..core import BugyoCloudClient, BugyoCloudClientError
from ..utils.formpostrequest import FormPostRequest
from .loginpage import LoginPage


class Authenticate(FormPostRequest):
    """ 認証します """

    def __init__(self, client: BugyoCloudClient, login_page: LoginPage):
        self.__client = client
        self.__token_value = login_page.token_value
        self.__top_url = ''
        super().__init__(login_page.action)

    @property
    def top_url(self) -> str:
        return self.__top_url

    def call(self, auth_info: AuthInfo):
        response = self.__post_auth_info(
            auth_info.login_id, auth_info.password)
        self.__parse_response(response)

    def __post_auth_info(self, login_id: str, password: str) -> Response:
        data = {
            'btnLogin': None,
            'OBCID': login_id,
            'Password_d1': None,
            'Password_d2': None,
            'Password_d3': None,
            'Password': password,
            '__RequestVerificationToken': self.__token_value,
            'X-Requested-With': 'XMLHttpRequest'
        }
        prepped = self.__client.prepare_request(self)
        prepped.data = data

        resp = self.__client.send(prepped)
        resp.raise_for_status()

        return resp

    def __parse_response(self, response: Response) -> None:
        json = response.json

        if 'RedirectURL' in json:
            self.__top_url = json['RedirectURL']
        else:
            raise BugyoCloudClientError(
                'Response is not to be expected.', json)
