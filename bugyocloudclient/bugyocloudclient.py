from requests import Request, Session
from bs4 import BeautifulSoup


class BugyoCloudClientError(Exception):
    """ 奉行クラウドHTTPクライアント用例外 """
    pass


class BugyoCloudClient:
    """ 奉行クラウドHTTPクライアント """
    USER_AGENT = 'Mozilla/5.0 ()'
    ENCODING = 'utf-8'

    def __init__(self, login_url: str):
        self.login_url = login_url
        self.session = Session()

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

    def __create_request(self, method: str, url: str):
        headers = {
            'User-Agent': BugyoCloudClient.USER_AGENT
        }
        return Request(method=method, url=url, headers=headers)

    def __parse_login_page(self, html):
        """ 認証用URLと、__RequestVerificationTokenを返す """
        soup = BeautifulSoup(html)

        loginform_ele = soup.select_one('#loginform')

        if loginform_ele is None:
            raise BugyoCloudClientError('Cannot find a element of #loginform ')

        token_ele = soup.select_one('input[name=__RequestVerificationToken]')

        if token_ele is None:
            raise BugyoCloudClientError(
                'Cannot find a element of __RequestVerificationToken')

        return (loginform_ele['action'], token_ele['value'])

    def __get_login_page(self):
        req = self.__create_request('GET', self.login_url)
        prepped = self.session.prepare_request(req)

        resp = self.session.send(prepped)
        resp.raise_for_status()

        return resp.content.decode(BugyoCloudClient.ENCODING)

    def __prepare_session_cookie(self, login_id: str):
        """ 'session'クッキーを内部的に保持するためだけに必要 """
        url = self.login_url+'/login/CheckAuthenticationMethod'
        req = self.__create_request('POST', url)
        prepped = self.session.prepare_request(req)
        prepped.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        prepped.data = {'OBCiD': login_id, 'isBugyoCloud': 'false'}

        resp = self.session.send(prepped)
        resp.raise_for_status()

    def __post_auth_info(self, url: str, token: str, login_id: str, password: str):
        data = {
            'btnLogin': None,
            'OBCID': login_id,
            'Password_d1': None,
            'Password_d2': None,
            'Password_d3': None,
            'Password': password,
            '__RequestVerificationToken': token,
            'X-Requested-With': 'XMLHttpRequest'
        }
        req = self.__create_request('POST', url)
        prepped = self.session.prepare_request(req)
        prepped.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        prepped.data = data

        resp = self.session.send(prepped)
        resp.raise_for_status()

        json = resp.json

        if 'RedirectURL' in json:
            return resp.json['RedirectURL']
        else:
            raise BugyoCloudClientError(
                'Response is not to be expected.', json)
