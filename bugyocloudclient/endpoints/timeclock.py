from logging import getLogger

from bugyocloudclient.core import BugyoCloudClient, BugyoCloudClientError
from bugyocloudclient.models.punchinfo import PunchInfo
from bugyocloudclient.utils.urlproducer import produce_url

logger = getLogger(__name__)


class TimeClock(object):
    """ 打刻します。 """

    def call(self, client: BugyoCloudClient, token: str, punch_info: PunchInfo) -> None:
        url = self.__get_url(client)
        headers = self.__create_headers(client, token)
        data = self.__create_data(punch_info)

        logger.debug('Trying to POST. url=%s headers=%s data=%s',
                     url, headers, data)

        resp = client.session.post(
            url=url, headers=headers, data=data, allow_redirects=False)
        resp.raise_for_status()

        if resp.status_code != 200:
            logger.error('Unexpected status code. status_code=%s content=%s',
                         resp.status_code, resp.content)
            raise BugyoCloudClientError('Unexpected status code.')

    def __get_url(self, client: BugyoCloudClient) -> str:
        key = type(self).__name__
        return produce_url(key, client.param)

    def __create_headers(self, client: BugyoCloudClient, token: str) -> dict:
        return {
            'Referer': self.__get_referer_url(client),
            '__RequestVerificationToken': token,
            'X-Requested-With': 'XMLHttpRequest',
        }

    def __get_referer_url(self, client: BugyoCloudClient) -> str:
        key = 'PunchmarkPage'
        return produce_url(key, client.param)

    def __create_data(self, punch_info: PunchInfo) -> dict:
        return {
            'ClockType': punch_info.clock_type.value,
            'LaborSystemID': '0',
            'LaborSystemCode': '',
            'LaborSystemName': '',
            'PositionLatitude': punch_info.latitude,
            'PositionLongitude': punch_info.longitude,
            'PositionAccuracy': '0',
        }
