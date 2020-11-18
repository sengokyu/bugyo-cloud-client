import requests


class BugyoCloudClientError(Exception):
    """ 奉行クラウドHTTPクライアント用例外 """
    pass


class BugyoCloudClient(requests.Session):
    """ 奉行クラウドHTTPクライアント """
    USER_AGENT = 'Mozilla/5.0 ()'
    ENCODING = 'utf-8'

    def __init__(self, login_url: str, login_id):
        self.login_url = login_url
        self.login_id = login_id
        super().__init__()

    def login(self, login_id: str, password: str):
        html = self.__get_login_page()
        (auth_url, token) = self.__parse_login_page(html)
        self.__prepare_session_cookie(login_id)
        redirect_url = self.__post_auth_info(
            auth_url, token, login_id, password)

        req = self.__create_request('GET', redirect_url)
        prepped = self.session.prepare_request(req)

        resp = self.session.send(prepped)

        return resp.ok()

    def __get_login_page(self):
        req = self.__create_request('GET', self.login_url)
        prepped = self.session.prepare_request(req)

        resp = self.session.send(prepped)
        resp.raise_for_status()

        return resp.content.decode(BugyoCloudClient.ENCODING)
