from typing import Generator

from cachetclient.base import Manager, Resource
from cachetclient.v1 import enums


class Component(Resource):
    pass


class ComponentManager(Manager):
    resource_class = Component
    path = 'components'

    def create(self, name, description=None, status=1, link=None, order=None, group_id=None, enabled=True):
        """
        Create a component.

        Params:
            name (str): Name of the component
            description (str): Description of the component
            status (int): Status if of the component
            link (str): Link to the component
            order (int): Order of the component in its group
            group_id (int): The group it belongs to
            enabled (bool): Enabled status

        Returns:
            Compotent instance
        """
        pass

    def list(self) -> Generator[Component, None, None]:
        yield from self._list_paginated(self.path)

    def delete(self, subscriber_id) -> None:
        self._delete(self.path, subscriber_id)

    def count(self) -> int:
        return self._count(self.path)
