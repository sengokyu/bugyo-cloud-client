from unittest import TestCase

from bugyocloudclient.endpoints.loginpageparser import LoginPageParser


class TestLoginPargeParser(TestCase):
    CONTENT = '''\
    <form id="loginform" action="http://example.com/">
    <input name="__RequestVerificationToken" value="token value">
    </form>'''

    def test_create_instance(self) -> None:
        """ インスタンスを生成 """
        # When
        instance = LoginPageParser(TestLoginPargeParser.CONTENT)

        # Then
        self.assertIsInstance(instance, LoginPageParser)

    def test_init(self) -> None:
        """ コンテンツをパース """
        # When
        instance = LoginPageParser(TestLoginPargeParser.CONTENT)

        # Then
        self.assertEqual('http://example.com', instance.action)
        self.assertEqual('token value', instance.token_value)
