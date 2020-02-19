from datetime import datetime
from unittest import mock
from requests.exceptions import HTTPError

from base import CachetTestcase
from fakeapi import FakeHttpClient
from cachetclient.v1 import enums


@mock.patch('cachetclient.client.HttpClient', new=FakeHttpClient)
class MetricsTests(CachetTestcase):

    @mock.patch('cachetclient.client.HttpClient', new=FakeHttpClient)
    def setUp(self):
        self.client = self.create_client()

    def test_get(self):
        first = self.client.metrics.create(name="Issue 1", description="Descr", suffix='IS')
        print(first.__dict__)
        self.client.metrics.create(name="Issue 2", description="Descr", suffix='IS2')
        self.client.metrics.create(name="Issue 3", description="Descr", suffix='IS3')

        self.assertEqual(self.client.metrics.count(), 3)

        metrics = self.client.metrics.list()
        metrics = list(metrics)
        self.assertEqual(len(metrics), 3)

        # Re-fetch a single metric
        metric = self.client.metrics.get(first.id)
        self.assertEqual(first.id, metric.id)

    def test_create(self):
        metric = self.client.metrics.create(
            name="Something blew up!",
            description="We are looking into it",
            suffix="SO"
        )

        self.assertEqual(metric.id, 1)
        self.assertEqual(metric.name, "Something blew up!")
        self.assertEqual(metric.description, "We are looking into it")
        self.assertEqual(metric.suffix, "SO")
        self.assertEqual(metric.default_value, 0)
        self.assertEqual(metric.display_chart, 0)
        self.assertIsInstance(metric.created_at, datetime)
        self.assertIsInstance(metric.updated_at, datetime)

        metric.delete()
