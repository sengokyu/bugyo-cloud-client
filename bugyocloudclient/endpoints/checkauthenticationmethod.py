from ..bugyocloudclient import BugyoCloudClient
from ..utils.baserequest import BaseRequest


class CheckAuthenticationMethod(object):
    """ 'session'クッキーをclientに読ませる """

    def __init__(self, client: BugyoCloudClient) -> None:
        self.client = client

    def post(self) -> None:
        self.__prepare_session_cookie()

    def __prepare_session_cookie(self) -> None:
        url = (self.client.login_url, '/login/CheckAuthenticationMethod')
        req = BaseRequest('POST', url)
        prepped = self.client.prepare_request(req)

        prepped.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        prepped.data = {
            'OBCiD': self.client.login_id,
            'isBugyoCloud': 'false'
        }

        resp = self.client.send(prepped)
        resp.raise_for_status()
