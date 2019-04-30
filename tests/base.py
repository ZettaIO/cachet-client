"""Simplify all tests"""
from unittest import TestCase, mock

import cachetclient
from fakeapi import FakeHttpClient


@mock.patch('cachetclient.httpclient.HttpClient', FakeHttpClient)
class CachetTestcase(TestCase):
    endpoint = 'https://status.example.com/api/v1'
    token = 's4cr337k33y'
