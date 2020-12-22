from .baserequest import BaseRequest


class GetRequest(BaseRequest):
    def __init__(self, url):
        super().__init__(method='GET', url=url)
