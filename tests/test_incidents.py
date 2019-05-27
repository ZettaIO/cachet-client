from datetime import datetime
from unittest import mock
from requests.exceptions import HTTPError

from base import CachetTestcase
from fakeapi import FakeHttpClient
from cachetclient.v1 import enums


@mock.patch('cachetclient.client.HttpClient', new=FakeHttpClient)
class IncidentTests(CachetTestcase):

    @mock.patch('cachetclient.client.HttpClient', new=FakeHttpClient)
    def setUp(self):
        self.client = self.create_client()

    def test_create(self):
        issue = self.client.incidents.create(
            "Something blew up!",
            "We are looking into it",
            enums.INCIDENT_INVESTIGATING,
        )
        self.assertEqual(issue.id, 1)
        self.assertEqual(issue.name, "Something blew up!")
        self.assertEqual(issue.message, "We are looking into it")
        self.assertEqual(issue.status, enums.INCIDENT_INVESTIGATING)
        self.assertEqual(issue.component_id, None)
        self.assertEqual(issue.visible, True)
        self.assertEqual(issue.notify, True)
        self.assertEqual(issue.human_status, 'Investigating')
        self.assertIsInstance(issue.created_at, datetime)
        self.assertIsInstance(issue.updated_at, datetime)
        self.assertIsInstance(issue.scheduled_at, datetime)
        issue.delete()
