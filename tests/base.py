"""Simplify all tests"""
from unittest import TestCase, mock

import cachetclient
from fakeapi import FakeHttpClient


class CachetTestcase(TestCase):
    endpoint = 'https://status.example.com/api/v1'
    token = 's4cr337k33y'

    def create_client(self) -> cachetclient.v1.Client:
        return cachetclient.Client(endpoint=self.endpoint, api_token=self.token)
