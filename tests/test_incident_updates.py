from unittest import mock
from datetime import datetime

from base import CachetTestcase
from fakeapi import FakeHttpClient
from cachetclient.v1 import enums


@mock.patch('cachetclient.client.HttpClient', new=FakeHttpClient)
class IncidentUpdatesTests(CachetTestcase):

    @mock.patch('cachetclient.client.HttpClient', new=FakeHttpClient)
    def setUp(self):
        self.client = self.create_client()

    def test_create(self):
        incident = self.client.incidents.create(
            "Boom!",
            "We are investigating",
            enums.INCIDENT_INVESTIGATING,
        )

        # Add 3 updates
        first = self.client.incident_updates.create(
            incident.id,
            enums.INCIDENT_IDENTIFIED,
            "We have located the issue",
        )
        # Test all properties
        self.assertEqual(first.id, 1)
        self.assertEqual(first.incident_id, 1)
        self.assertEqual(first.status, enums.INCIDENT_IDENTIFIED)
        self.assertEqual(first.message, "We have located the issue")
        self.assertEqual(first.user_id, 1)
        self.assertIsInstance(first.created_at, datetime)
        self.assertIsInstance(first.updated_at, datetime)
        self.assertEqual(first.human_status, "Identified")
        self.assertIsInstance(first.permlink, str)

        self.client.incident_updates.create(
            incident.id,
            enums.INCIDENT_WATCHING,
            "We have located the issue"
        )
        self.client.incident_updates.create(
            incident.id,
            enums.INCIDENT_FIXED,
            "We have located the issue"
        )

        self.assertEqual(self.client.incident_updates.count(incident.id), 3)

        # List and compare
        updates = list(incident.updates())
        self.assertEqual(len(updates), 3)
        self.assertEqual(
            [{k: i.attrs[k] for k in ['id', 'incident_id', 'status', 'message']} for i in updates],
            [{'id': 1, 'incident_id': 1, 'status': 2, 'message': 'We have located the issue'},
            {'id': 2, 'incident_id': 1, 'status': 3, 'message': 'We have located the issue'},
            {'id': 3, 'incident_id': 1, 'status': 4, 'message': 'We have located the issue'}]
        )

        # Update an entry
        entry = updates[-1]
        entry.status = enums.INCIDENT_INVESTIGATING
        entry.message = "Lookin into it.."
        entry.update()

        # Manually re-fetch
        updated_entry = self.client.incident_updates.get(entry.incident_id, entry.id)
        self.assertEqual(updated_entry.status, enums.INCIDENT_INVESTIGATING)
        self.assertEqual(updated_entry.message, "Lookin into it..")
