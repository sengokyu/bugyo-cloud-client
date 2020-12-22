from .tasks.abtask import ABTask
from requests import Session


class BugyoCloudClientError(Exception):
    """ 奉行クラウドHTTPクライアント用例外 """
    pass


class BugyoCloudClient(Session):
    """ 奉行クラウドHTTPクライアント """
    USER_AGENT = 'Mozilla/5.0 ()'
    ENCODING = 'utf-8'

    def __init__(self, tenant_code: str):
        self.__tenant_code = tenant_code
        super().__init__()

    @property
    def tenant_code(self):
        return self.__tenant_code

    def exec(self, abtask: ABTask) -> None:
        abtask.execute(self)
