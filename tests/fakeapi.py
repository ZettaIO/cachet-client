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


class FakePing(FakeData):
    def request(self, *args, **kwargs):
        return { "data": "Pong!" }


class FakeVersion(FakeData):

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
            (r'^ping', self.ping, ['GET']),
            (r'^version', self.version, ['GET']),
            (r'^component/groups/(?P<group_id>\w+)', self.components, ['GET', 'POST', 'DELETE']),
            (r'^component/groups', self.components, ['GET', 'POST']),
            (r'^components/(?P<component_id>\w+)', self.components, ['GET', 'POST', 'DELETE']),
            (r'^components', self.components, ['GET', 'POST']),
            (r'^incidents/(?P<incident_id>/updates/(?P<update_id>', ['GET', 'POST', 'DELETE']),
            (r'^incident/(?P<incident_id>\w+)/updates', self.incident_updates, ['GET', 'POST']),
            (r'^incidents', self.incidents, ['GET', 'POST']),
            (r'^metric/points', self.metric_points),
            (r'^metrics', self.metrics),
            (r'^subscribers', self.subscribers),
        ]

    def dispatch(self, method, path, data=None, params=None):
        for route in self._routes:
            pass


class FakeHttpClient:
    """Fake implementation of the httpclient"""

    def __init__(self, base_url, api_token, timeout=None, verify_tls=True, user_agent=None):
        self.routes = Routes()
        self.base_url = base_url
        self.api_token = api_token
        self.timeout = timeout
        self.verify_tls = verify_tls
        self.user_agent = user_agent

    def get(self, path, params=None):
        return self.request('GET', path, params=params)

    def post(self, path, data=None, params=None):
        return self.request('POST', path, data=data, params=params)

    def delete(self, path):
        return self.request('DELETE', path)

    def request(self, method, path, params=None, data=None):
        return self.routes.dispatch(method, path, params=params, data=data)


if __name__ == '__main__':
    client = FakeHttpClient('http://status.example.com', 's4cr337k33y')
