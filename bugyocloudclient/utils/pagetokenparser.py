from bugyocloudclient.core import BugyoCloudClientError
from bs4 import BeautifulSoup


def parse_token(html: str) -> str:
    """ ページ中にある__RequestVerificationTokenを返します """

    bs = BeautifulSoup(html, 'html.parser')

    token_ele = bs.select_one(
        'input[name=__RequestVerificationToken]')

    if token_ele is None:
        raise BugyoCloudClientError(
            'Cannot find an element of __RequestVerificationToken')

    token_value = token_ele.get('value')

    if token_value is None:
        raise BugyoCloudClientError(
            'Cannot find an attribute of value in the __RequestVerificationToken')

    return token_value
