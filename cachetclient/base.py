

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

    def __init__(self, client):
        self._http = client
