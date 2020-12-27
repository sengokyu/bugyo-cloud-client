from bugyocloudclient.tasks.basetask import BaseTask
from bugyocloudclient import BugyoCloudClient
from bugyocloudclient.models.clientparam import ClientParam
from requests import Session


class BugyoCloudClientTests():
    def test_create_instance(self) -> None:
        # Given
        tenant_code = 'tete'

        # When
        instance = BugyoCloudClient(tenant_code)

        # Then
        assert isinstance(instance, BugyoCloudClient)
        assert isinstance(instance.param, ClientParam)
        assert isinstance(instance.session, Session)
        assert instance.param.tenant_code == tenant_code

    def test_exec(self, mocker):
        """ タスクを実行します。 """    
        # Given
        tenant_code = 'tete'
        task = mocker.Mock(BaseTask)
        instance = BugyoCloudClient(tenant_code)

        # When
        instance.exec(task)

        # Then
        task.execute.assert_called_once_with(instance)
