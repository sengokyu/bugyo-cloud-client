from enum import Enum


class ClockType(Enum):
    """ 打刻種別 """
    clock_in = "ClockIn"
    clock_out = "ClockOut"


class PunchInfo(object):
    """
    打刻情報
    """

    def __init__(self):
        """
        cTor
        """
        self.__clock_type = None
        self.__latitude = 0
        self.__longitude = 0

    @property
    def clock_type(self) -> ClockType:
        return self.__clock_type

    @clock_type.setter
    def clock_type(self, value: ClockType) -> None:
        self.__clock_type = value

    @property
    def latitude(self) -> float:
        return self.__latitude

    @latitude.setter
    def latitude(self, value: float) -> None:
        self.__latitude = value

    @property
    def longitude(self) -> float:
        return self.__longitude

    @longitude.setter
    def longitude(self, value: float) -> None:
        self.__longitude = value
