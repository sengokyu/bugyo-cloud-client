from bugyocloudclient.core import BugyoCloudClient
from bugyocloudclient.endpoints.punchmarkpage import PunchmarkPage
from bugyocloudclient.endpoints.timeclock import TimeClock
from bugyocloudclient.models.punchinfo import PunchInfo
from bugyocloudclient.tasks.basetask import BaseTask


class PunchTask(BaseTask):
    """
    打刻します。
    """

    def __init__(self, punch_info: PunchInfo):
        """
        cTor
        """
        self.__punch_info = punch_info

    def execute(self, client: BugyoCloudClient) -> None:
        """
        打刻します。
        """
        punchmark_page = PunchmarkPage()
        token = punchmark_page.call(client)

        time_clock = TimeClock()
        time_clock.call(client, token, self.__punch_info)
