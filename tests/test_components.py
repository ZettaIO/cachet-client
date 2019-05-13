from unittest import mock

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
        self.assertEqual(comp.status, enums.COMPONENT_OPERATIONAL)
        self.assertIsNotNone(comp.created_at)
        self.assertIsNotNone(comp.updated_at)
        self.assertIsNone(comp.deleted_at)

    def test_delete(self):
        pass
