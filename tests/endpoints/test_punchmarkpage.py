from bugyocloudclient import BugyoCloudClient
from bugyocloudclient.endpoints.punchmarkpage import PunchmarkPage
from bugyocloudclient.models.clientparam import ClientParam
from requests.models import Response


class TestPunchmarkPage():

    def test_create_instance(self, mocker) -> None:
        # When
        instance = PunchmarkPage()

        # Then
        assert isinstance(instance, PunchmarkPage)

    def test_call(self, mocker) -> None:
        """ パースしてtoken_valueが返ります。 """
        # Given
        instance = PunchmarkPage()
        client = mocker.Mock(spec=BugyoCloudClient)
        resp = mocker.Mock(Response)
        tenant_code = 'tete'
        user_code = 'usus'
        param = ClientParam(tenant_code)
        param.user_code = user_code
        content = '<input type="hidden" name="__RequestVerificationToken" value="a token">'

        resp.content = bytearray(content, 'utf-8')
        client.session.get.return_value = resp
        client.param = param

        # When
        actual = instance.call(client)

        # Then
        assert actual == 'a token'
        expected_url = 'https://hromssp.obc.jp/{0}/{1}/timeclock/punchmark/'.format(
            tenant_code, user_code)
        client.session.get.assert_called_once_with(expected_url)
