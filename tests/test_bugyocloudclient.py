from bugyocloudclient import BugyoCloudClient


class BugyoCloudClientTests():
    LOGIN_URL = 'https://example.com/foobar'
    LOGIN_ID = 'login id'

    def test_create_instance(self) -> None:
        # When
        actual = BugyoCloudClient(
            BugyoCloudClientTests.LOGIN_URL, BugyoCloudClientTests.LOGIN_ID)

        # Then
        assert isinstance(actual, BugyoCloudClient)
