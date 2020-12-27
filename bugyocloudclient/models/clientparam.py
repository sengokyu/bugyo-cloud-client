class ClientParam(object):
    """
    アクセス用の情報コンテナです。
    """

    def __init__(self, tenant_code):
        """
        cTor.
        """
        self.__tenant_code = tenant_code
        self.__user_code = ''  # ログイン後TOPURLパスの2要素目

    @property
    def tenant_code(self) -> str:
        """
        テナント識別子
        """
        return self.__tenant_code

    @property
    def user_code(self) -> str:
        """ ログイン後TOPURLパスの2要素目 """
        return self.__user_code

    @user_code.setter
    def user_code(self, value: str) -> None:
        """ ログイン後TOPURLパスの2要素目 """
        self.__user_code = value
