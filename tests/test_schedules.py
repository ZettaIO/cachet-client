import types

from requests.exceptions import HTTPError
from unittest import mock
from datetime import datetime

from base import CachetTestcase
from fakeapi import FakeHttpClient
from cachetclient.v1 import enums


@mock.patch('cachetclient.client.HttpClient', new=FakeHttpClient)
class SchedulerTests(CachetTestcase):

    @mock.patch('cachetclient.client.HttpClient', new=FakeHttpClient)
    def setUp(self):
        self.client = self.create_client()

    def test_create(self):
        start_time = datetime.strptime('2020-09-07 00:18:00', '%Y-%m-%d %H:%M:%S')
        instance = self.client.schedules.create(
            name="Planned Maintenance",
            status=enums.SCHEDULE_STATUS_UPCOMING,
            message="We're doing some maintenance today",
            scheduled_at=start_time,
        )

        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.status, enums.SCHEDULE_STATUS_UPCOMING)
        self.assertEqual(instance.name, "Planned Maintenance")
        self.assertEqual(instance.message, "We're doing some maintenance today")
        self.assertEqual(instance.scheduled_at, start_time)
        self.assertEqual(instance.completed_at, None)

        instance.delete()

    def test_list(self):
        start_time = datetime.strptime('2020-09-07 00:18:00', '%Y-%m-%d %H:%M:%S')
        for i in range(20):
            self.client.schedules.create(
                name="Planned Maintenance",
                status=enums.SCHEDULE_STATUS_UPCOMING,
                message="We're doing some maintenance today",
                scheduled_at=start_time,
            )

        self.assertEqual(self.client.schedules.count(), 20)
        self.assertIsInstance(self.client.schedules.list(), types.GeneratorType)
        instance = next(self.client.schedules.list(page=2, per_page=10))
        self.assertEqual(instance.id, 11)
