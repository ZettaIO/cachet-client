from unittest import mock, TestCase

import cachetclient
from base import CachetTestcase
from fakeapi import FakeHttpClient


@mock.patch('cachetclient.client.HttpClient', new=FakeHttpClient)
class ClientTests(CachetTestcase):

    def test_mock(self):
        client = cachetclient.Client(endpoint=self.endpoint, api_token=self.token)
        self.assertTrue(client._http.is_fake_client)

    def test_basic(self):
        """Create a basic client"""
        cachetclient.Client(endpoint=self.endpoint, api_token=self.token)

    def test_endpoint_no_version(self):
        """Supply an endpoint without version"""
        with self.assertRaises(ValueError):
            cachetclient.Client(endpoint="meh", api_token=self.token)

    def test_endpoint_supply_version(self):
        """Test supplying modifier url through proxy etc"""
        cachetclient.Client(endpoint="https://status", version='1', api_token=self.token)

    def test_enviroment_vars(self):
        """Instantiate client using env vars"""
        envs = {'CACHET_API_TOKEN': self.token, 'CACHET_ENDPOINT': self.endpoint}
        with mock.patch.dict('os.environ', envs):
            cachetclient.Client()

    def test_missing_token(self):
        """Missing token raises error"""
        with self.assertRaises(ValueError):
            cachetclient.Client(endpoint=self.endpoint)

    def test_missing_endpoint(self):
        """Missing endpoint raises error"""
        with self.assertRaises(ValueError):
            cachetclient.Client(api_token=self.token)

    def test_missing_endpoint_env(self):
        """Missing endpoint env var should raise error"""
        envs = {'CACHET_API_TOKEN': self.token}
        with mock.patch.dict('os.environ', envs):
            with self.assertRaises(ValueError):
                cachetclient.Client()

    def test_missing_token_env(self):
        """Missing token env var should raise error"""
        envs = {'CACHET_ENDPOINT': self.endpoint}
        with mock.patch.dict('os.environ', envs):
            with self.assertRaises(ValueError):
                cachetclient.Client()
