from .baserequest import BaseRequest


class FormPostRequest(BaseRequest):
    def __init__(self, url: str):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        super().__init__('POST', url, headers)
