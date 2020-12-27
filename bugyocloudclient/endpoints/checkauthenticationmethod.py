from bugyocloudclient import BugyoCloudClient
from bugyocloudclient.models.authinfo import AuthInfo
from bugyocloudclient.utils.urlproducer import produce_url


class CheckAuthenticationMethod(object):
    """ 
    'session'クッキーをclientに読ませる
     """

    def call(self, client: BugyoCloudClient, auth_info: AuthInfo) -> None:
        url = self.__get_url(client)
        data = {
            'OBCiD': auth_info.login_id,
            'isBugyoCloud': 'false'
        }

        resp = client.session.post(url=url, data=data)
        resp.raise_for_status()

    def __get_url(self, client: BugyoCloudClient) -> str:
        key = type(self).__name__
        return produce_url(key, client.param)
