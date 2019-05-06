from unittest import mock

from base import CachetTestcase
import cachetclient
from fakeapi import FakeHttpClient


@mock.patch('cachetclient.client.HttpClient', new=FakeHttpClient)
class SubscriberTests(CachetTestcase):

    def test_create(self):
        client = self.create_client()
        client.subscribers.create_or_update('user@example.com')

        # Count subscribers
        count = client.subscribers.count()
        self.assertEqual(count, 1)

        # Inspect subscribers
        subs = list(client.subscribers.list())
        sub = subs[0]
        self.assertEqual(sub.id, 1)

        # Delete subscriber
        sub.delete()
        count = client.subscribers.count()
        self.assertEqual(count, 0)

    def test_list(self):
        client = self.create_client()
        for i in range(20 * 4 + 5):
            pass
