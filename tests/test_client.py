from unittest import TestCase, mock

import cachetclient
from fakeapi import FakeHttpClient

ENDPOINT = 'https://status.example.com/api/v1'
TOKEN = 's4cr337k33y'


@mock.patch('cachetclient.httpclient.HttpClient', FakeHttpClient)
class ClientTests(TestCase):

    def test_basic(self):
        """Create a basic client"""
        cachetclient.Client(endpoint=ENDPOINT, api_token=TOKEN)

    def test_endpoint_no_version(self):
        """Supply an endpoint without version"""
        with self.assertRaises(ValueError):
            cachetclient.Client(endpoint="meh", api_token=TOKEN)

    def test_endpoint_supply_version(self):
        """Test supplying modifier url through proxy etc"""
        cachetclient.Client(endpoint="https://status", version='1', api_token=TOKEN)

    def test_enviroment_vars(self):
        """Instantiate client using env vars"""
        envs = {'CACHET_API_TOKEN': TOKEN, 'CACHET_ENDPOINT': ENDPOINT}
        with mock.patch.dict('os.environ', envs):
            cachetclient.Client()

    def test_missing_token(self):
        """Missing token raises error"""
        with self.assertRaises(ValueError):
            cachetclient.Client(endpoint=ENDPOINT)

    def test_missing_endpoint(self):
        """Missing endpoint raises error"""
        with self.assertRaises(ValueError):
            cachetclient.Client(api_token=TOKEN)

    def test_missing_endpoint_env(self):
        """Missing endpoint env var should raise error"""
        envs = {'CACHET_API_TOKEN': TOKEN}
        with mock.patch.dict('os.environ', envs):
            with self.assertRaises(ValueError):
                cachetclient.Client()

    def test_missing_token_env(self):
        """Missing token env var should raise error"""
        envs = {'CACHET_ENDPOINT': ENDPOINT}
        with mock.patch.dict('os.environ', envs):
            with self.assertRaises(ValueError):
                cachetclient.Client()
