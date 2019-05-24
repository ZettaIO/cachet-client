from datetime import datetime
from unittest import mock
from requests.exceptions import HTTPError

from base import CachetTestcase
from fakeapi import FakeHttpClient
from cachetclient.v1 import enums


@mock.patch('cachetclient.client.HttpClient', new=FakeHttpClient)
class ComponentGroupTests(CachetTestcase):

    def test_count(self):
        """Count groups"""
        client = self.create_client()
        self.assertEqual(client.component_groups.count(), 0)

    def test_create(self):
        """Create and obtain groups"""
        client = self.create_client()
        client.component_groups.create("Global Services")
        self.assertEqual(client.component_groups.count(), 1)

        group = next(client.component_groups.list())
        self.assertEqual(group.id, 1)
        self.assertEqual(group.name, "Global Services")
        self.assertEqual(group.collapsed, enums.COMPONENT_GROUP_COLLAPSED_FALSE)
        self.assertEqual(group.order, 0)
        self.assertIsInstance(group.created_at, datetime)
        self.assertIsNotNone(group.updated_at, datetime)
        self.assertFalse(group.is_collapsed, False)
        self.assertTrue(group.is_open)
        self.assertTrue(group.is_operational)

        group = client.component_groups.get(1)
        self.assertEqual(group.id, 1)

    def test_get_nonexist(self):
        client = self.create_client()
        with self.assertRaises(HTTPError):
            client.component_groups.get(1337)

    def test_delete(self):
        """Create and delete component"""
        client = self.create_client()
        client.component_groups.create("Global Services")
        self.assertEqual(client.component_groups.count(), 1)
        group = next(client.component_groups.list())
        group.delete()
        self.assertEqual(client.component_groups.count(), 0)

    def test_delete_nonexist(self):
        """Delete non-exsitent component"""
        client = self.create_client()
        with self.assertRaises(HTTPError):
            client.component_groups.delete(1337)

    def test_self_update(self):
        """Test self updating resource"""
        client = self.create_client()
        client.component_groups.create("Global Services")
        group = next(client.component_groups.list())
        group.name = "Global Stuff"
        group.order = 1
        group.collapsed = enums.COMPONENT_GROUP_COLLAPSED_TRUE

        new_group = group.update()
        self.assertEqual(new_group.id, 1)
        self.assertEqual(new_group.name, "Global Stuff")
        self.assertEqual(new_group.order, 1)
        self.assertEqual(new_group.collapsed, enums.COMPONENT_GROUP_COLLAPSED_TRUE)
