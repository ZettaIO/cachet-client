import types
from unittest import mock

from base import CachetTestcase
import cachetclient
from fakeapi import FakeHttpClient


@mock.patch('cachetclient.client.HttpClient', new=FakeHttpClient)
class SubscriberTests(CachetTestcase):

    def test_ping(self):
        client = self.create_client()

        result = client.ping()
        self.assertTrue(result)

        result = client.ping.get()
        self.assertTrue(result)
