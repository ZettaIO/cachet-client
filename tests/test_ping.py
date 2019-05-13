from unittest import mock

from base import CachetTestcase
import cachetclient
from fakeapi import FakeHttpClient


@mock.patch('cachetclient.client.HttpClient', new=FakeHttpClient)
class SubscriberTests(CachetTestcase):

    def test_ping_call(self):
        """Ping using __call__ method"""
        client = self.create_client()
        result = client.ping()
        self.assertTrue(result)

    def test_ping_get(self):
        """Ping using get method"""
        client = self.create_client()
        result = client.ping.get()
        self.assertTrue(result)
