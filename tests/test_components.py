from unittest import mock
from requests.exceptions import HTTPError

from base import CachetTestcase
from fakeapi import FakeHttpClient
from cachetclient.v1 import enums


@mock.patch('cachetclient.client.HttpClient', new=FakeHttpClient)
class ComponentsTests(CachetTestcase):

    @mock.patch('cachetclient.client.HttpClient', new=FakeHttpClient)
    def setUp(self):
        self.client = self.create_client()

    def create_component(self, client):
        return client.components.create(
            "API Server",
            enums.COMPONENT_STATUS_OPERATIONAL,
            description="General API server",
        )

    def test_count(self):
        """Count components"""
        client = self.create_client()
        self.assertEqual(client.components.count(), 0)

    def test_create(self):
        """Create and obtain component"""
        self.create_component(self.client)
        self.assertEqual(self.client.components.count(), 1)

        comp = next(self.client.components.list())
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

        comp = self.client.components.get(1)
        self.assertEqual(comp.id, 1)

    def test_delete(self):
        """Create and delete component"""
        self.create_component(self.client)
        self.assertEqual(self.client.components.count(), 1)
        comp = next(self.client.components.list())
        comp.delete()
        self.assertEqual(self.client.components.count(), 0)

    def test_delete_nonexist(self):
        """Delete non-exsitent component"""
        with self.assertRaises(HTTPError):
            self.client.components.delete(1337)

    def test_tags(self):
        """Test tags"""
        comp = self.create_component(self.client)
        comp.add_tag('test')
        self.assertTrue(comp.has_tag('test'))
        self.assertFalse(comp.has_tag('thing'))
        comp.del_tag('test')
        self.assertFalse(comp.has_tag('test'))

        comp.add_tag('tag1')
        comp.add_tag('tag2')
        comp = comp.update()
        self.assertTrue(comp.has_tag('tag1'))
        self.assertTrue(comp.has_tag('tag2'))
        self.assertFalse(comp.has_tag('test'))
        self.assertEqual(comp.tags, {'tag1', 'tag2'})
