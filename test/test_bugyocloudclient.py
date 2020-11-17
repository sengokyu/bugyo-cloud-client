import unittest
import os
from bugyo_cloud_client import BugyoCloudClient

class BugyoCloudClientTests(unittest.TestCase):
    def setUp(self) -> None:
        self.login_url = os.getenv('OBC_LOGIN_URL') or exit(
            'OBC_LOGIN_URL environment var required.')
        self.login_id = os.getenv('OBC_LOGIN_ID') or exit(
            'OBC_LOGIN_ID environemnt var required.')
        self.password = os.getenv('OBC_PASSWORD') or exit(
            'OBC_PASSWORD environment var required.')

    def test_login(self):
        # Given
        client = BugyoCloudClient(self.login_url)


if __name__ == '__main__':
    unittest.main()
