from bugyocloudclient.bugyocloudclient import BugyoCloudClientError
from bs4 import BeautifulSoup


class LoginPageParser:
    """ ログインページのパーサです。 """

    def __init__(self, html: str):
        self.bs = BeautifulSoup(html, 'html.parser')
        self.action = self.__parse_action()
        self.token_value = self.__parse_token()

    def __parse_action(self) -> str:
        """ 認証用URLを返す """
        loginform_ele = self.bs.select_one('#loginform')
        if (loginform_ele is None):
            raise BugyoCloudClientError(
                'Cannot find an element of #loginform ')

        action = loginform_ele.get('action')
        if (action is None):
            raise BugyoCloudClientError(
                'Cannot find an attribute of action in the #loginform')

        return action

    def __parse_token(self) -> str:
        """ __RequestVerificationTokenを返す """

        token_ele = self.bs.select_one(
            'input[name=__RequestVerificationToken]')
        if (token_ele is None):
            raise BugyoCloudClientError(
                'Cannot find an element of __RequestVerificationToken')

        token_value = token_ele.get('value')
        if (token_value is None):
            raise BugyoCloudClientError(
                'Cannot find an attribute of value in the __RequestVerificationToken')

        return token_value
