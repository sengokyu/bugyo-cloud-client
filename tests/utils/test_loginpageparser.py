from bugyocloudclient.utils.loginpageparser import LoginPageParser


class TestLoginPargeParser():
    CONTENT = '''\
    <form id="loginform" action="http://example.com/">
    <input name="__RequestVerificationToken" value="token value">
    </form>'''

    def test_create_instance(self) -> None:
        """ インスタンスを生成 """
        # When
        instance = LoginPageParser(TestLoginPargeParser.CONTENT)

        # Then
        assert isinstance(instance, LoginPageParser)

    def test_init(self) -> None:
        """ コンテンツをパース """
        # When
        instance = LoginPageParser(TestLoginPargeParser.CONTENT)

        # Then
        assert instance.action == 'http://example.com/'
        assert instance.token_value == 'token value'
