"""Fake cachet api"""
import math
import random
import re
import string

from requests.exceptions import HTTPError
from cachetclient.v1 import enums


class FakeData:

    def __init__(self, routes):
        self.routes = routes
        self.data = []
        self.map = {}
        self.last_id = 0

    def add_entry(self, entry):
        """Add a data entry"""
        self.data.append(entry)
        self.map[entry['id']] = entry

    def get_by_id(self, resource_id):
        """Get a resource by id"""
        resource_id = int(resource_id)
        data = self.map.get(resource_id)
        if data is None:
            raise HTTPError("404")

        return data

    def delete_by_id(self, resource_id):
        """Delete a resource"""
        resource_id = int(resource_id)
        resource = self.map.get(resource_id)
        if not resource:
            raise HTTPError("404")

        del self.map[resource_id]
        self.data.remove(resource)

    def next_id(self):
        """Generate unique instance id"""
        self.last_id += 1
        return self.last_id

    def _get(self, resource_id):
        """Get a single resource"""
        resource_id = int(resource_id)
        data = self.get_by_id(resource_id)
        return FakeHttpResponse(data={'data': data})

    def _list(self, per_page=20, page=1, filter_data=None):
        """Generic list with pagination"""
        start = per_page * (page - 1)
        end = per_page * page

        # Filter data on a single key/value pair
        data = self.data
        if filter_data:
            item = filter_data.popitem()
            data = [i for i in self.data if item in i.items()]

        entries = data[start:end]

        return FakeHttpResponse(
            data={
                'meta': {
                    'pagination': {
                        'total': len(self.data),
                        'count': len(entries),
                        'per_page': per_page,
                        'current_page': page,
                        'total_pages': math.ceil(len(self.data) / per_page),
                    }
                },
                'data': entries,
            }
        )


class FakeSubscribers(FakeData):

    def get(self, params=None, **kwargs):
        """List only supported"""
        return super()._list(
            per_page=params.get('per_page') or 20,
            page=params.get('page') or 1,
        )

    def post(self, params=None, data=None):
        instance = {
            "id": self.next_id(),
            "email": data['email'],
            "verify_code": ''.join(random.choice(string.ascii_lowercase) for i in range(16)),
            "verified_at": "2015-07-24 14:42:24",
            "created_at": "2015-07-24 14:42:24",
            "updated_at": "2015-07-24 14:42:24",
            "global": True,
        }
        self.add_entry(instance)
        return FakeHttpResponse(data={'data': instance})

    def delete(self, subscriber_id=None, **kwargs):
        self.delete_by_id(subscriber_id)
        return FakeHttpResponse()


class FakeComponents(FakeData):

    def get(self, component_id=None, params=None, **kwargs):
        if component_id is None:
            return super()._list(
                per_page=params.get('per_page') or 20,
                page=params.get('page') or 1,
            )
        else:
            return super()._get(component_id)

    def post(self, params=None, data=None):
        instance = {
            "id": self.next_id(),
            "name": data.get('name'),
            "description": data.get('description'),
            "link": data.get('link'),
            "status": data.get('status'),
            "status_name": "Operational",
            "order": data.get('order'),
            "group_id": data.get('group_id'),
            "created_at": "2015-08-01 12:00:00",
            "updated_at": "2015-08-01 12:00:00",
            "deleted_at": None,
            "tags": self._transform_tags(data.get('tags'))
        }
        self.add_entry(instance)
        return FakeHttpResponse(data={'data': instance})

    def put(self, component_id=None, params=None, data=None):
        # TODO: Rules on what field can be updated
        instance = self.get_by_id(component_id)
        instance.update(data)
        instance['tags'] = self._transform_tags(instance.get('tags'))
        return FakeHttpResponse(data={'data': instance})

    def delete(self, component_id=None, params=None, data=None):
        self.delete_by_id(component_id)
        return FakeHttpResponse()

    def _transform_tags(self, tags):
        return {v: v for v in tags.split(',')} if tags else None


class FakeComponentGroups(FakeData):

    def get(self, group_id=None, params=None, **kwargs):
        if group_id is None:
            return super()._list(
                per_page=params.get('per_page') or 20,
                page=params.get('page') or 1,
            )
        else:
            return super()._get(group_id)

    def post(self, params=None, data=None):
        instance = {
            'id': self.next_id(),
            'name': data.get('name'),
            'order': data.get('order'),
            'collapsed': data.get('collapsed'),
            'updated_at': '2015-11-07 16:35:13',
            'created_at': '2015-11-07 16:35:13',
        }
        self.add_entry(instance)
        return FakeHttpResponse(data={'data': instance})

    def put(self, group_id=None, params=None, data=None):
        # TODO: Rules on what field can be updated
        instance = self.get_by_id(group_id)
        instance.update(data)
        return FakeHttpResponse(data={'data': instance})

    def delete(self, group_id=None, params=None, data=None):
        self.delete_by_id(group_id)
        return FakeHttpResponse()


class FakeIncidents(FakeData):

    def get(self, incident_id=None, params=None, data=None):
        if incident_id:
            return self._get(incident_id)
        else:
            return self._list(
                per_page=params.get('per_page') or 20,
                page=params.get('page') or 1,
            )

    def post(self, params=None, data=None):
        # Fields we don't store but instead triggers behaviour
        # 'component_status': data.get('component_status'),
        # 'template': data.get('template'),
        # 'vars': data.get('vars'),
        instance = {
            'id': self.next_id(),
            'name': data.get('name'),
            'message': data.get('message'),
            'status': data.get('status'),
            'human_status': enums.incident_status_human(data.get('status')),
            'visible': data.get('visible'),
            'component_id': data.get('component_id'),
            'notify': data.get('notify'),
            'created_at': '2019-05-25 15:21:34',
            'scheduled_at': '2019-05-25 15:21:34',
            'updated_at': '2019-05-25 15:21:34',
        }
        self.add_entry(instance)
        return FakeHttpResponse(data={'data': instance})

    def put(self, incident_id=None, params=None, data=None):
        # TODO: Rules on what field can be updated
        instance = self.get_by_id(incident_id)

        # Required params
        instance['name'] = data['name']
        instance['message'] = data['message']
        instance['status'] = data['status']
        instance['visible'] = data['visible']
        # Optional only update if value is present
        for key, value in data.items():
            if key in instance and value is not None:
                instance[key] = value

        return FakeHttpResponse(data={'data': instance})

    def delete(self, incident_id=None, params=None, data=None):
        self.delete_by_id(incident_id)
        return FakeHttpResponse()


class FakeIncidentUpdates(FakeData):

    def post(self, incident_id=None, params=None, data=None):
        new_id = self.next_id()
        instance = {
            'id': new_id,
            'incident_id': int(incident_id),
            'status': data['status'],
            'human_status': enums.incident_status_human(data['status']),
            'message': data['message'],
            'user_id': 1,  # We assume user 1 always
            'permalink': 'http://status.test/incidents/1#update-{}'.format(new_id),
            'created_at': '2019-05-25 15:21:34',
            'updated_at': '2019-05-25 15:21:34',
        }
        self.add_entry(instance)
        return FakeHttpResponse(data={'data': instance})

    def put(self, incident_id=None, update_id=None, params=None, data=None):
        instance = self.get_by_id(update_id)
        print("data", data)
        instance.update({
            'status': data['status'],
            'message': data['message'],
        })
        return FakeHttpResponse(data={'data': instance})

    def get(self, incident_id=None, update_id=None, params=None, data=None):
        if update_id is None:
            return super()._list(
                per_page=params.get('per_page') or 20,
                page=params.get('page') or 1,
            )
        else:
            return super()._get(update_id)


class FakePing(FakeData):

    def get(self, *args, **kwargs):
        return FakeHttpResponse(data={"data": "Pong!"})


class FakeVersion(FakeData):

    def get(self, *args, **kwargs):
        return FakeHttpResponse(data={
            "meta": {
                "on_latest": True,
                "latest": {
                    "tag_name": "v2.3.10",
                    "prelease": False,
                    "draft": False,
                }
            },
            "data": "2.3.11-dev",
        })


class Routes:
    """Requesting routing"""

    def __init__(self):
        self.ping = FakePing(self)
        self.version = FakeVersion(self)
        self.components = FakeComponents(self)
        self.component_groups = FakeComponentGroups(self)
        self.incidents = FakeIncidents(self)
        self.incident_updates = FakeIncidentUpdates(self)
        self.metrics = None
        self.metric_points = None
        self.subscribers = FakeSubscribers(self)

        self._routes = [
            (r'^ping', self.ping, ['get']),
            (r'^version', self.version, ['get']),
            (r'^components/groups/(?P<group_id>\w+)', self.component_groups, ['get', 'put', 'delete']),
            (r'^components/groups', self.component_groups, ['get', 'post']),
            (r'^components/(?P<component_id>\w+)', self.components, ['get', 'post', 'put', 'delete']),
            (r'^components', self.components, ['get', 'post']),
            (r'^incidents/(?P<incident_id>\w+)/updates/(?P<update_id>\w+)', self.incident_updates, ['get', 'post', 'put', 'delete']),
            (r'^incidents/(?P<incident_id>\w+)/updates', self.incident_updates, ['get', 'post']),
            (r'^incidents/(?P<incident_id>\w+)', self.incidents, ['get', 'put', 'delete']),
            (r'^incidents', self.incidents, ['get', 'post']),
            (r'^metric/points', self.metric_points, ['get']),
            (r'^metrics', self.metrics, ['get']),
            (r'^subscribers/(?P<subscriber_id>\w+)', self.subscribers, ['delete']),
            (r'^subscribers', self.subscribers, ['get', 'post']),
        ]

    def dispatch(self, method, path, data=None, params=None):
        for route in self._routes:
            pattern, manager, allowed_methods = route
            # print(pattern, manager, allowed_methods)

            match = re.search(pattern, path)
            if not match:
                continue

            if method in allowed_methods:
                func = getattr(manager, method, None)
                if func:
                    return func(params=params, data=data, **match.groupdict())

            raise ValueError("Method '{}' not allowed for '{}'".format(method, path))


class FakeHttpClient:
    """Fake implementation of the httpclient"""
    is_fake_client = True

    def __init__(self, base_url, api_token, timeout=None, verify_tls=True, user_agent=None):
        self.routes = Routes()
        self.base_url = base_url
        self.api_token = api_token
        self.timeout = timeout
        self.verify_tls = verify_tls
        self.user_agent = user_agent

    def get(self, path, params=None):
        return self.request('get', path, params=params)

    def post(self, path, data=None, params=None):
        return self.request('post', path, data=data, params=params)

    def put(self, path, data=None, params=None):
        return self.request('put', path, data=data, params=params)

    def delete(self, path, resource_id):
        return self.request('delete', "{}/{}".format(path, resource_id))

    def request(self, method, path, params=None, data=None):
        return self.routes.dispatch(method, path, params=params, data=data)


class FakeHttpResponse:

    def __init__(self, data=None, status_code=200):
        self.status_code = status_code
        self._data = data

    def json(self):
        return self._data

    def raise_for_status(self):
        if self.status_code > 300:
            raise HTTPError(self.status_code)


if __name__ == '__main__':
    client = FakeHttpClient('http://status.example.com', 's4cr337k33y')
    client.post('subscribers', data={'email': 'user@example.com'})
    subs = client.get('subscribers')
    print("Subscribers:", subs)
    client.delete('subscribers', subs[0]['id'])
    print("Subscribers:", subs)
