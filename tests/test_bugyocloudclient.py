import unittest
import os
from bugyocloudclient import BugyoCloudClient


class BugyoCloudClientTests(unittest.TestCase):
    LOGIN_URL = 'https://example.com/foobar'
    instance: BugyoCloudClient

    def setUp(self) -> None:
        self.instance = BugyoCloudClient(self.LOGIN_URL)

    def test_create_instance(self) -> None:
        # Then
        self.assertIsInstance(self.instance, BugyoCloudClient)
