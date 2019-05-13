from unittest import mock

from base import CachetTestcase
from fakeapi import FakeHttpClient


@mock.patch('cachetclient.client.HttpClient', new=FakeHttpClient)
class VersionTests(CachetTestcase):

    def test_version_call(self):
        """Version using __call__ method"""
        client = self.create_client()
        self.check_result(client.version())

    def test_version_get(self):
        """Version using get method"""
        client = self.create_client()
        self.check_result(client.version.get())

    def check_result(self, version):
        """Test version resource values"""
        self.assertEqual(version.value, "2.3.11-dev")
        self.assertEqual(version.on_latest, True)
        self.assertEqual(
            version.latest,
            {
                "tag_name": "v2.3.10",
                "prelease": False,
                "draft": False,
            },
        )
