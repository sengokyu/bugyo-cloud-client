from bugyocloudclient.utils.pagetokenparser import parse_token


class TestPargeTokenParser():
    CONTENT = '''\
    <form id="loginform" action="http://example.com/">
    <input name="__RequestVerificationToken" value="token value">
    </form>'''

    def test_parse(self) -> None:
        """ コンテンツをパース """
        # When
        token = parse_token(TestPargeTokenParser.CONTENT)

        # Then
        assert token == 'token value'
