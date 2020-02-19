from unittest import mock
from datetime import datetime

from base import CachetTestcase
from fakeapi import FakeHttpClient
from cachetclient.v1 import enums


@mock.patch('cachetclient.client.HttpClient', new=FakeHttpClient)
class MetricPointsTest(CachetTestcase):

    @mock.patch('cachetclient.client.HttpClient', new=FakeHttpClient)
    def setUp(self):
        self.client = self.create_client()

    def test_create(self):
        metric = self.client.metrics.create(
            name="Issue 1",
            description="Descr",
            suffix='IS',
            default_value=0
        )

        # Add 3 updates
        first = self.client.metric_points.create(
            metric_id=metric.id,
            value=1,
        )
        # Test all properties
        self.assertEqual(first.id, 1)
        self.assertEqual(first.metric_id, 1)
        self.assertEqual(first.value, 1)
        self.assertIsInstance(first.created_at, datetime)
        self.assertIsInstance(first.updated_at, datetime)

        # Add to check_list for later testing
        check_list = [{'id': first.id, 'metric_id': 1, 'value': first.value}]

        # create a couple of entries
        for point in range(1, 3):
            self.client.metric_points.create(
                metric_id=metric.id,
                value=point+1,
            )
            # Append to check_list for later testing
            check_list.append({'id': point+1, 'metric_id': 1, 'value': point+1})

        self.assertEqual(self.client.metric_points.count(metric.id), 3)

        # List and compare
        points = list(metric.points())
        self.assertEqual(len(points), 3)
        self.assertEqual(
            [{k: i.attrs[k] for k in ['id', 'metric_id', 'value']} for i in points],
            check_list
        )
