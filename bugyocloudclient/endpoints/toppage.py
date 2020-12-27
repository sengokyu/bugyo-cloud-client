from pathlib import PurePath
from urllib.parse import urlparse

from bugyocloudclient import BugyoCloudClient
from bugyocloudclient.core import BugyoCloudClientError


class TopPage(object):

    def call(self, client: BugyoCloudClient, url: str) -> str:
        """
        user_codeをセットします。
        """
        resp = client.session.get(url)
        return self.__extract_user_code(resp.url)

    def __extract_user_code(self, url: str) -> str:
        """ urlからuser codeを取り出します。 """
        path = urlparse(url).path
        parts = PurePath(path).parts
        if len(parts) < 3:
            raise BugyoCloudClientError('Unexpected url ', url)

        return parts[2]
