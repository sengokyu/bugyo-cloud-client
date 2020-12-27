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

    @property
    def clock_type(self) -> ClockType:
        return self.__clock_type

    @clock_type.setter
    def clock_type(self, value: ClockType) -> None:
        self.__clock_type = value
