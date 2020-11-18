from requests.models import Response
from ..bugyocloudclient import BugyoCloudClient, BugyoCloudClientError
from ..utils.baserequest import BaseRequest


class Authenticate(object):
    """ 認証します """

    def __init__(self, client: BugyoCloudClient, auth_url: str) -> None:
        self.client = client
        self.auth_url = auth_url

    def post(self, token: str, password: str) -> None:
        self.__parse_response(self.__post_auth_info(token, password))

    def __post_auth_info(self, token: str, password: str) -> Response:
        data = {
            'btnLogin': None,
            'OBCID': self.client.login_id,
            'Password_d1': None,
            'Password_d2': None,
            'Password_d3': None,
            'Password': password,
            '__RequestVerificationToken': token,
            'X-Requested-With': 'XMLHttpRequest'
        }
        req = BaseRequest('POST', self.auth_url)
        prepped = self.client.prepare_request(req)

        prepped.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        prepped.data = data

        resp = self.client.send(prepped)
        resp.raise_for_status()

        return resp

    def __parse_response(self, resp: Response) -> None:
        json = resp.json

        if 'RedirectURL' in json:
            self.redirect_url = resp.json['RedirectURL']
        else:
            raise BugyoCloudClientError(
                'Response is not to be expected.', json)
