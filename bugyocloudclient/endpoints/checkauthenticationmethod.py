from ..authinfo import AuthInfo
from ..core import BugyoCloudClient
from ..utils.formpostrequest import FormPostRequest


class CheckAuthenticationMethod(FormPostRequest):
    """ 'session'クッキーをclientに読ませる """

    def __init__(self, client: BugyoCloudClient):
        self.__client = client
        super().__init__(self.__build_url())

    def call(self, auth_info: AuthInfo) -> None:
        self.__prepare_session_cookie(auth_info.login_id)

    def __prepare_session_cookie(self, login_id: str) -> None:
        prepped = self.__client.prepare_request(self)

        prepped.data = {
            'OBCiD': login_id,
            'isBugyoCloud': 'false'
        }

        resp = self.__client.send(prepped)
        resp.raise_for_status()

    def __build_url(self) -> str:
        return ('https://id.obc.co.jp/', self.__client.tenant_code, '/login/CheckAuthenticationMethod')
