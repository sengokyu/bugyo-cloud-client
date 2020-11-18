from abc import ABC


class ABTask(ABC):
    """ タスクのinterfaceです。抽象基底クラス(ABC) にしています。 """

    def prepare():
        """ 準備処理 """
        pass

    def execute():
        """ 実処理 """
        pass

    def finish():
        """ 終了処理 """
        pass
