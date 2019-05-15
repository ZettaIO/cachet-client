from unittest import mock
from requests.exceptions import HTTPError

from base import CachetTestcase
from fakeapi import FakeHttpClient
from cachetclient.v1 import enums


@mock.patch('cachetclient.client.HttpClient', new=FakeHttpClient)
class ComponentsTests(CachetTestcase):

    def test_count(self):
        """Count components"""
        client = self.create_client()
        self.assertEqual(client.components.count(), 0)

    def test_create(self):
        """Create and obtain component"""
        client = self.create_client()
        client.components.create(
            "API Server",
            description="General API server",
        )
        self.assertEqual(client.components.count(), 1)

        comp = next(client.components.list())
        self.assertEqual(comp.id, 1)
        self.assertEqual(comp.name, "API Server")
        self.assertEqual(comp.description, "General API server")
        self.assertEqual(comp.group_id, None)
        self.assertEqual(comp.link, None)
        self.assertEqual(comp.status, enums.COMPONENT_STATUS_OPERATIONAL)
        self.assertEqual(comp.status_name, "Operational")
        self.assertIsNotNone(comp.created_at)
        self.assertIsNotNone(comp.updated_at)
        self.assertIsNone(comp.deleted_at)

        comp = client.components.get(1)
        self.assertEqual(comp.id, 1)

    def test_delete(self):
        """Create and delete component"""
        client = self.create_client()
        client.components.create(
            "API Server",
            description="General API server",
        )
        self.assertEqual(client.components.count(), 1)
        comp = next(client.components.list())
        comp.delete()
        self.assertEqual(client.components.count(), 0)

    def test_delete_nonexist(self):
        """Delete non-exsitent component"""
        client = self.create_client()
        with self.assertRaises(HTTPError):
            client.components.delete(1337)
