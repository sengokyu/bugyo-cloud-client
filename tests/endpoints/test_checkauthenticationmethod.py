from bugyocloudclient.authinfo import AuthInfo
from bugyocloudclient.core import BugyoCloudClient
from bugyocloudclient.endpoints.checkauthenticationmethod import CheckAuthenticationMethod


class TestCheckAuthenticationMethod:
    def test_create_instance(self, mocker):
        # Given
        client = mocker.Mock(spec=BugyoCloudClient)

        # When
        instance = CheckAuthenticationMethod(client)

        # Then
        assert isinstance(instance, CheckAuthenticationMethod)

    def test_call(self, mocker):
        # Given
        client = mocker.Mock(spec=BugyoCloudClient)
        auth_info = mocker.Mock(spec=AuthInfo)
        instance = CheckAuthenticationMethod(client)

        # When
        instance.call(auth_info)

        # Then
        client.prepare_request.assert_called_with(instance)
        client.send.assert_called_once()
