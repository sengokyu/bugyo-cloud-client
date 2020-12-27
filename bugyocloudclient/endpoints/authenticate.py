from bugyocloudclient.utils.urlproducer import produce_url
from bugyocloudclient import BugyoCloudClient, BugyoCloudClientError
from bugyocloudclient.models.authinfo import AuthInfo
from requests import Response


class Authenticate(object):
    """ 認証します """

    def call(self, client: BugyoCloudClient, token: str, auth_info: AuthInfo) -> str:
        """ RedirectURLを返します。 """
        url = self.__get_url(client)
        data = self.__create_data(token, auth_info)
        resp = client.session.post(url=url, data=data)
        resp.raise_for_status()

        return self.__parse_response(resp)

    def __create_data(self, token: str, auth_info: AuthInfo) -> Response:
        return {
            'btnLogin': None,
            'OBCID': auth_info.login_id,
            'Password_d1': None,
            'Password_d2': None,
            'Password_d3': None,
            'Password': auth_info.password,
            '__RequestVerificationToken': token,
            'X-Requested-With': 'XMLHttpRequest'
        }

    def __parse_response(self, response: Response) -> None:
        json = response.json

        if 'RedirectURL' in json:
            return json['RedirectURL']
        else:
            raise BugyoCloudClientError(
                'Response is not to be expected.', json)

    def __get_url(self, client: BugyoCloudClient) -> str:
        key = type(self).__name__
        return produce_url(key, client.param)
