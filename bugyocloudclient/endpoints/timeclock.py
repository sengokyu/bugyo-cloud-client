from bugyocloudclient.core import BugyoCloudClient
from bugyocloudclient.models.punchinfo import PunchInfo
from bugyocloudclient.utils.urlproducer import produce_url


class TimeClock(object):
    """ 打刻します。 """

    def call(self, client: BugyoCloudClient, token: str, punch_info: PunchInfo) -> None:
        url = self.__get_url(client)
        data = self.__create_data(punch_info)
        resp = client.session.post(url=url, data=data)
        resp.raise_for_status()

    def __get_url(self, client: BugyoCloudClient) -> str:
        key = type(self).__name__
        return produce_url(key, client.param)

    def __create_data(self, punch_info: PunchInfo) -> dict:
        return {
            'ClockType': punch_info.clock_type.value,
            'LaborSystemID': '0',
            'LaborSystemCode': '',
            'LaborSystemName': '',
            'PositionLatitude': 0,
            'PositionLongitude': 0,
            'PositionAccuracy': '0',
        }
