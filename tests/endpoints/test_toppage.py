import pytest
from bugyocloudclient import BugyoCloudClient
from bugyocloudclient.core import BugyoCloudClientError
from bugyocloudclient.endpoints.authenticate import Authenticate
from bugyocloudclient.endpoints.toppage import TopPage
from requests import Response


class TestsTopPage:
    def test_create_instance(self):
        """　インスタンス生成します。 """
        # When
        instance = TopPage()

        # Then
        assert isinstance(instance, TopPage)

    def test_call(self, mocker):
        """ URLからuser_codeを返します。 """
        # Given
        instance = TopPage()
        client = mocker.Mock(BugyoCloudClient)
        url = 'https://id.example.com'
        resp = mocker.Mock(Response)
        user_code = 'p2'

        resp.url = 'http://example.com/p1/{0}/'.format(user_code)
        client.session.get.return_value = resp

        # When
        actual = instance.call(client, url)

        # Then
        assert actual == user_code
        client.session.get.assert_called_once_with(url)

    def test_call_error(self, mocker):
        """ URLが期待通りでない時はエラー """
        # Given
        instance = TopPage()
        client = mocker.Mock(BugyoCloudClient)
        url = 'https://id.example.com'
        resp = mocker.Mock(Response)

        resp.url = 'http://example.com/p1/'
        client.session.get.return_value = resp

        with pytest.raises(BugyoCloudClientError):
            # When
            instance.call(client, url)
