from typing import Generator, Set
from datetime import datetime

from cachetclient.base import Manager, Resource
from cachetclient.v1 import enums
from cachetclient import utils


class Component(Resource):

    def __init__(self, manager, data):
        super().__init__(manager, data)
        if data.get('tags') is None:
            data['tags'] = {}

    @property
    def id(self) -> int:
        """int: The unique ID of the component"""
        return self._data['id']

    @property
    def name(self) -> str:
        """str: Get or set name of the component"""
        return self._data['name']

    @name.setter
    def name(self, value: str):
        self._data['name'] = value

    @property
    def description(self) -> str:
        """str: Get or set component description"""
        return self.get('description')

    @description.setter
    def description(self, value: str):
        self._data['description'] = value

    @property
    def link(self) -> str:
        """str: Get or set http link to the component"""
        return self._data['link']

    @link.setter
    def link(self, value: str):
        self._data['link'] = value

    @property
    def status(self) -> int:
        """int: Get or set dtatus id of the component (see :py:data:`enums`)"""
        return self._data['status']

    @status.setter
    def status(self, value: int):
        self._data['status'] = value

    @property
    def status_name(self) -> str:
        """str: Human readable status representation"""
        return self._data['status_name']

    @property
    def order(self) -> int:
        """int: Get or set order of the component in a group"""
        return self._data['order']

    @order.setter
    def order(self, value: int):
        self._data['order'] = value

    @property
    def group_id(self) -> int:
        """int: Get or set the component group id"""
        return self._data['group_id']

    @group_id.setter
    def group_id(self, value: int):
        self._data['group_id'] = value

    @property
    def enabled(self) -> bool:
        """bool: Get or set enabled state"""
        return self._data['enabled']

    @enabled.setter
    def enabled(self, value: bool):
        self._data['enabled'] = value

    @property
    def tags(self) -> set:
        """set: Get or set tags for the component

        Also see :py:data:`add_tag`, :py:data:`del_tag` and :py:data:`has_tag` methods.
        """
        return set(self._data['tags'].keys()) if self._data['tags'] else set()

    @tags.setter
    def tags(self, value: set):
        self._data['tags'] = {val: val for val in value}

    @property
    def created_at(self) -> datetime:
        """datetime: When the component was created"""
        return utils.to_datetime(self.get('created_at'))

    @property
    def updated_at(self) -> datetime:
        """datetime: Last time the component was updated"""
        return utils.to_datetime(self.get('updated_at'))

    def add_tag(self, name: str) -> None:
        """Add a new tag.

        Args:
            name (str): Name of the tag
        """
        self._data['tags'][name] = name

    def del_tag(self, name: str) -> None:
        """Delete a tag.

        Args:
            name (str): Name of tag to remove

        Raises:
            KeyError: if tag does not exist
        """
        del self._data['tags'][name]

    def has_tag(self, name: str) -> bool:
        """Check if a tag exists.

        Args:
            name (str): Tag name

        Returns:
            bool: If the tag exists
        """
        return name in self.get('tags')


class ComponentManager(Manager):
    resource_class = Component
    path = 'components'

    def create(
            self,
            *,
            name: str,
            status: int,
            description: str = None,
            link: str = None,
            order: int = None,
            group_id: int = None,
            enabled: bool = True,
            tags: Set[str] = None):
        """Create a component.

        Keyword Args:
            name (str): Name of the component
            status (int): Status if of the component (see enums module)
            description (str): Description of the component (required)
            link (str): Link to the component
            order (int): Order of the component in its group
            group_id (int): The group it belongs to
            enabled (bool): Enabled status
            tags (list): String tags

        Returns:
            :py:class:`Component` instance
        """
        if status not in enums.COMPONENT_STATUS_LIST:
            raise ValueError("Invalid status id '{}'. Valid values :{}".format(
                status,
                enums.COMPONENT_STATUS_LIST,
            ))

        return self._create(
            self.path,
            {
                'name': name,
                'description': description,
                'status': status,
                'link': link,
                'order': order,
                'group_id': group_id,
                'enabled': enabled,
                'tags': tags,
            }
        )

    def update(
            self,
            component_id: int,
            *,
            status: int,
            name: str = None,
            description: str = None,
            link: str = None,
            order: int = None,
            group_id: int = None,
            enabled: bool = None,
            tags: Set[str] = None,
            **kwargs) -> Component:
        """Update a component by id.

        Args:
            component_id (int): The component to update

        Keyword Args:
            status (int): Status of the component (see enums)
            name (str): New name
            description (str): New description
            link (str): Link to component
            order (int): Order in component group
            group_id (int): Component group id
            enabled (bool): Enable status of component
            tags (list): List of strings

        Returns:
            Updated Component from server
        """
        return self._update(
            self.path,
            component_id,
            self._build_data_dict(
                status=status,
                name=name,
                description=description,
                link=link,
                order=order,
                group_id=group_id,
                enabled=enabled,
                tags=','.join(tags) if tags else None,
            ),
        )

    def list(self, page: int = 1, per_page: int = 20) -> Generator[Component, None, None]:
        """List all components

        Keyword Args:
            page (int): The page to start listing
            per_page (int): Number of entries per page

        Returns:
            Generator of Component instances
        """
        yield from self._list_paginated(self.path, page=page, per_page=per_page)

    def get(self, component_id: int) -> Component:
        """Get a component by id

        Args:
            component_id (int): Id of the component

        Returns:
            Component instance

        Raises:
            HttpError: if not found
        """
        return self._get(self.path, component_id)

    def delete(self, component_id: int) -> None:
        """Delete a component

        Args:
            component_id (int): Id of the component

        Raises:
            HTTPError: if component do not exist
        """
        self._delete(self.path, component_id)

    def count(self) -> int:
        """Count the number of components

        Returns:
            int: Total number of components
        """
        return self._count(self.path)
