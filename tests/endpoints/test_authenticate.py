from bugyocloudclient.endpoints.authenticate import Authenticate
from bugyocloudclient.endpoints.loginpage import LoginPage
from bugyocloudclient.core import BugyoCloudClient


class TestAuthenticate:
    def test_create_instance(self, mocker):
        # Given
        client = mocker.Mock(spec=BugyoCloudClient)
        login_page = mocker.Mock(spec=LoginPage)

        # When
        instance = Authenticate(client, login_page)

        # Then
        assert isinstance(instance, Authenticate)
