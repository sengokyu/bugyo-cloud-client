from logging import getLogger

from bugyocloudclient import BugyoCloudClient, BugyoCloudClientError
from bugyocloudclient.config import CONTENT_ENCODING
from bugyocloudclient.models.authinfo import AuthInfo
from bugyocloudclient.utils.urlproducer import produce_url

logger = getLogger(__name__)


class CheckAuthenticationMethod(object):
    """
    'session'クッキーをclientに読ませる
     """

    def call(self, client: BugyoCloudClient, token: str, auth_info: AuthInfo) -> None:
        url = self.__get_url(client)
        headers = {
            '__RequestVerificationToken': token,
            'X-Requested-With': 'XMLHttpRequest',
        }
        data = {
            'OBCiD': auth_info.login_id,
            'isBugyoCloud': 'false'
        }

        logger.debug('Trying to POST. url=%s headrs=%s data=%s',
                     url, headers, data)

        resp = client.session.post(
            url=url, headers=headers, data=data, allow_redirects=False)
        resp.raise_for_status()

        if resp.status_code != 200:
            content = resp.content
            logger.critical(
                'Unexpected status code and response. status_code=%s content=%s', resp.status_code, content)
            raise BugyoCloudClientError('Unexpected status code.')

    def __get_url(self, client: BugyoCloudClient) -> str:
        key = type(self).__name__
        return produce_url(key, client.param)
