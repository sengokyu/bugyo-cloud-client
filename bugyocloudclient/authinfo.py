class AuthInfo:
    def __init__(self, login_id: str, password: str):
        self.__login_id = login_id
        self.__password = password

    @property
    def login_id(self) -> str:
        return self.__login_id

    @property
    def password(self) -> str:
        return self.__password
