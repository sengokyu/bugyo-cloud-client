from typing import Tuple
from ..core import BugyoCloudClientError
from bs4 import BeautifulSoup


class LoginPageParser:
    """ ログインページのパーサです。 """

    def parse(self, html: str) -> Tuple[str, str]:
        bs = BeautifulSoup(html, 'html.parser')
        return (self.__parse_action(bs), self.__parse_token(bs))

    def __parse_action(self, bs: BeautifulSoup) -> str:
        """ 認証用URLを返す """
        loginform_ele = bs.select_one('#loginform')
        if (loginform_ele is None):
            raise BugyoCloudClientError(
                'Cannot find an element of #loginform ')

        action = loginform_ele.get('action')
        if (action is None):
            raise BugyoCloudClientError(
                'Cannot find an attribute of action in the #loginform')

        return action

    def __parse_token(self, bs: BeautifulSoup) -> str:
        """ __RequestVerificationTokenを返す """

        token_ele = bs.select_one(
            'input[name=__RequestVerificationToken]')
        if (token_ele is None):
            raise BugyoCloudClientError(
                'Cannot find an element of __RequestVerificationToken')

        token_value = token_ele.get('value')
        if (token_value is None):
            raise BugyoCloudClientError(
                'Cannot find an attribute of value in the __RequestVerificationToken')

        return token_value
