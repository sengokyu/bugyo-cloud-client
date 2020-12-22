from bugyocloudclient.utils.loginpageparser import LoginPageParser


class TestLoginPargeParser():
    CONTENT = '''\
    <form id="loginform" action="http://example.com/">
    <input name="__RequestVerificationToken" value="token value">
    </form>'''

    def test_create_instance(self) -> None:
        """ インスタンスを生成 """
        # When
        instance = LoginPageParser()

        # Then
        assert isinstance(instance, LoginPageParser)

    def test_parse(self) -> None:
        """ コンテンツをパース """
        # Given
        instance = LoginPageParser()

        # When
        (action, token) = instance.parse(TestLoginPargeParser.CONTENT)

        # Then
        assert action == 'http://example.com/'
        assert token == 'token value'
