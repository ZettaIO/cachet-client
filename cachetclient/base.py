

class Resource:
    """Bag of attributes"""
    def __init__(self, manager, data):
        self._manager = manager
        self._data = data

    def __repr__(self):
        return str(self)

    def get(self, name):
        """Obtain any attribute name for the resource"""
        return self._data.get(name)

    def delete(self):
        self._manager.delete(self.get('id'))


class Manager:
    resource_class = None
    path = None

    def __init__(self, client):
        self._http = client

        if self.resource_class is None:
            raise ValueError('resource_class not defined in class {}'.format(self.__class__))

        if self.path is None:
            raise ValueError('path not defined for class {}'.format(self.__class__))

    def _list_paginated(self, path, page_size=20):
        page = 1
        while True:
            result = self._http.get(
                path,
                params={'page': page, 'per_page': page_size},
            )
            json_data = result.json()

            meta = json_data['meta']
            data = json_data['data']

            for entry in data:
                yield self.resource_class(self, entry)

            if page >= meta['pagination']['total_pages']:
                break

            page += 1

    def _get(self, path, resource_id):
        result = self._http.get("{}/{}".format(path, resource_id))
        json_data = result.json()
        return self.resource_class(json_data['data'])

    def _count(self, path):
        result = self._http.get(path, params={'per_page': 1})
        json_data = result.json()
        return json_data['meta']['pagination']['total']

    def _delete(self, path, resource_id):
        self._http.delete(path, resource_id)
