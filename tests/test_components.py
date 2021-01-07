from datetime import datetime
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

    def create_component(
            self,
            client,
            status=enums.COMPONENT_STATUS_OPERATIONAL,
            name="API Server",
            description="General API server"):

        return client.components.create(
            name=name,
            status=status,
            description=description,
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
        self.assertIsInstance(comp.created_at, datetime)
        self.assertIsInstance(comp.updated_at, datetime)

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
        """Delete non-existant component"""
        with self.assertRaises(HTTPError):
            self.client.components.delete(1337)

    def test_tags(self):
        """Test tags"""
        comp = self.create_component(self.client)
        comp.add_tag('Test Tag')
        self.assertTrue(comp.has_tag(name='Test Tag'))
        self.assertTrue(comp.has_tag(name='test tag'))
        self.assertFalse(comp.has_tag(name='thing'))
        comp.del_tag(name="Test Tag")
        self.assertFalse(comp.has_tag("Test Tag"))

        comp.add_tag('Tag 1')
        comp.add_tag('Tag 2')
        comp = comp.update()
        self.assertTrue(comp.has_tag('Tag 1'))
        self.assertTrue(comp.has_tag('Tag 2'))
        self.assertTrue(comp.has_tag(slug='tag-1'))
        self.assertTrue(comp.has_tag(slug='tag-2'))
        self.assertFalse(comp.has_tag('test'))
        self.assertEqual(sorted(comp.tag_names), ["Tag 1", "Tag 2"])

        comp.add_tag("Tag 3")
        self.assertEqual(len(comp.tags), 3)
        comp.del_tag(slug="tag-1")
        self.assertEqual(len(comp.tags), 2)
        comp.update()
        self.assertFalse(comp.has_tag(slug="tag-1"))
        self.assertFalse(comp.has_tag(name="tag 1"))
        self.assertTrue(comp.has_tag(slug="tag-2"))
        self.assertTrue(comp.has_tag(name="tag 2"))
        self.assertTrue(comp.has_tag(slug="tag-3"))
        self.assertTrue(comp.has_tag(name="tag 3"))
        self.assertEqual(len(comp.tags), 2)
