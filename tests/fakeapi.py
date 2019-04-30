"""Fake cachet api"""
import re


class FakeData:

    def __init__(self, routes, data=None):
        self.routes = routes
        self.data = data or []


class FakeSubscribers(FakeData):

    def get(self):
        pass

    def list(self):
        pass

    def create(self):
        pass

    def delete(self):
        pass

    def request(self):
        pass


class FakeComponents(FakeData):
    def request(self):
        print("moo")


class FakePing:
    def request(self, *args, **kwargs):
        return { "data": "Pong!" }


class FakeVersion:

    def request(self, *args, **kwargs):
        return {
            "meta": {
                "on_latest": True,
                "latest": {
                    "tag_name": "v2.3.10",
                    "prelease": False,
                    "draft": False
                }
            },
            "data": "2.3.11-dev"
        }


class Routes:
    """Requesting routing"""

    def __init__(self):
        self.ping = FakePing(self)
        self.version = FakeVersion(self)
        self.components = FakeComponents(self)
        self.component_groups = None
        self.incidents = None
        self.incident_updates = None
        self.metrics = None
        self.metric_points = None
        self.subscribers = None

        self._routes = [
            (r'^ping', self.ping),
            (r'^version', self.version),
            (r'^component/groups', self.components),
            (r'^components/(?P<component_id>\w+)', self.components, ['GET', 'POST', 'DELETE']),
            (r'^components', self.components, ['GET', 'POST']),
            (r'^incident/updates', self.incident_updates),
            (r'^incidents', self.incidents),
            (r'^metric/points', self.metric_points),
            (r'^metrics', self.metrics),
            (r'^subscribers', self.subscribers),
        ]

    def dispatch(self, path, method):
        for route in self._routes:
            pass


class FakeHttpClient:
    """Fake implementation of the httpclient"""

    def __init__(self, base_url, api_token, timeout=None, verify_tls=True, user_agent=None):
        self.base_url = base_url
        self.api_token = api_token
        self.timeout = timeout
        self.verify_tls = verify_tls
        self.user_agent = user_agent

    def get(self, path, params=None):
        pass

    def post(self, path, data):
        pass

    def delete(self, path, resource_id):
        pass

    def request(self, method, path, params=None, data=None):
        pass

    def _resources(self, url):
        pass


# api/v1/*
# ping
# version
# components
# components/groups
