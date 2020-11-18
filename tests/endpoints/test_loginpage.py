from unittest.case import TestCase
from unittest.mock import Mock, patch

from bugyocloudclient.bugyocloudclient import BugyoCloudClient
from bugyocloudclient.endpoints.loginpage import LoginPage


class TestLoginPage(TestCase):
    @patch('bugyocloudclient.BugyoCloudClient')
    def test_create_instance(self, client: BugyoCloudClient) -> None:
        # Given
        client.login_url = 'https://example.com/login'

        # When
        instance = LoginPage(client)

        # Then
        client.prepare_request.assert_called_once()
        client.send.assert_called_once()
