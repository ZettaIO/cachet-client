from unittest import mock

from base import CachetTestcase
import cachetclient
from fakeapi import FakeHttpClient


@mock.patch('cachetclient.client.HttpClient', new=FakeHttpClient)
class SubscriberTests(CachetTestcase):

    def test_create(self):
        client = self.create_client()
        client.subscribers.create_or_update('user@example.com')

        count = client.subscribers.count()
        self.assertEqual(count,  1)

        subs = client.subscribers.list()
        subs = list(subs)
        sub = subs[0]
        self.assertEqual(sub.id, 1)
