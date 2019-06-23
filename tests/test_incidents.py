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

    def test_get(self):
        first = self.client.incidents.create(name="Issue 1", message="Descr", status=enums.INCIDENT_INVESTIGATING)
        self.client.incidents.create(name="Issue 2",  message="Descr", status=enums.INCIDENT_INVESTIGATING)
        self.client.incidents.create(name="Issue 3",  message="Descr", status=enums.INCIDENT_INVESTIGATING)

        self.assertEqual(self.client.incidents.count(), 3)

        incidents = self.client.incidents.list()
        incidents = list(incidents)
        self.assertEqual(len(incidents), 3)

        # Re-fetch a single issue
        incident = self.client.incidents.get(first.id)
        self.assertEqual(first.id, incident.id)

    def test_create(self):
        issue = self.client.incidents.create(
            name="Something blew up!",
            message="We are looking into it",
            status=enums.INCIDENT_INVESTIGATING,
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

        # Do an update on the resource
        issue.name = "Something probably blew up?!"
        issue = issue.update()
        self.assertEqual(issue.name, "Something probably blew up?!")

        # Update directly
        issue = self.client.incidents.update(
            issue.id,
            name="Something probably blew up?!",
            message="All good",
            status=enums.INCIDENT_FIXED,
            visible=True,
        )
        self.assertEqual(issue.id, 1)
        self.assertEqual(issue.status, enums.INCIDENT_FIXED)
        self.assertIsInstance(issue.created_at, datetime)
        self.assertIsInstance(issue.updated_at, datetime)
        self.assertIsInstance(issue.scheduled_at, datetime)

        issue.delete()
