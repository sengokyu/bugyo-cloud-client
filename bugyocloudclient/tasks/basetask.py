from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..core import BugyoCloudClient


class BaseTask(ABC):
    """ タスクのinterfaceです。抽象基底クラス(ABC) にしています。 """

    def prepare(self, client: 'BugyoCloudClient'):
        """ 準備処理 """
        pass

    def execute(self, client: 'BugyoCloudClient'):
        """ 実処理 """
        pass

    def finish(self, client: 'BugyoCloudClient'):
        """ 終了処理 """
        pass
