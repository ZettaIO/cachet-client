from unittest import mock

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
        incident.updates()

    def test_list(self):
        pass

    def test_delete(self):
        pass
