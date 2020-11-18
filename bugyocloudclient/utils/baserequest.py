from bugyocloudclient.bugyocloudclient import BugyoCloudClient
import requests


class BaseRequest(requests.Request):
    """ Requestベースクラス """

    def __init__(self, method: str, url: str):
        headers = {
            'User-Agent': BugyoCloudClient.USER_AGENT
        }
        super().__init__(method=method, url=url)
