from requests import Session

from bugyocloudclient.models.clientparam import ClientParam
from bugyocloudclient.tasks.basetask import BaseTask


class BugyoCloudClientError(Exception):
    """ 奉行クラウドHTTPクライアント用例外 """
    pass


class BugyoCloudClient(object):
    """ 奉行クラウドHTTPクライアント """

    def __init__(self, tenant_code: str):
        self.__param = ClientParam(tenant_code)
        self.__session = self.__create_session()

    @property
    def session(self) -> Session:
        return self.__session

    @property
    def param(self) -> ClientParam:
        return self.__param

    def exec(self, task: BaseTask) -> None:
        """ タスクを実行します。 """
        task.execute(self)

    def __create_session(self) -> Session:
        session = Session()
        session.headers = {
            'User-Agent': BugyoCloudClient.USER_AGENT
        }
        return session
