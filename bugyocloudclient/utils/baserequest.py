from ..core import BugyoCloudClient
from requests import Request


class BaseRequest(Request):
    """ Requestベースクラス """

    def __init__(self, method: str, url: str, headers: dict = None):
        if headers is None:
            headers = {}

        headers['User-Agent'] = BugyoCloudClient.USER_AGENT
        super().__init__(method=method, url=url, headers=headers)
