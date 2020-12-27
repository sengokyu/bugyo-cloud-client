from abc import ABC, abstractmethod

from bugyocloudclient import BugyoCloudClient
from bugyocloudclient.config import CONTENT_ENCODING
from bugyocloudclient.utils.pagetokenparser import parse_token
from bugyocloudclient.utils.urlproducer import produce_url


class TokenPage(ABC):
    """
    __RequestVerificationTokenがあるページです。
    """

    def call(self, client: BugyoCloudClient) -> str:
        url = self.__get_url(client)
        resp = client.session.get(url)
        resp.raise_for_status()
        content = resp.content.decode(CONTENT_ENCODING)

        return parse_token(content)

    def __get_url(self, client: BugyoCloudClient) -> str:
        """
        URLを返します。
        """
        key = type(self).__name__
        return produce_url(key, client.param)
