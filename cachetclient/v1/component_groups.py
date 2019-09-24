from datetime import datetime
from typing import Generator, List

from cachetclient.base import Manager, Resource
from cachetclient import utils
from cachetclient.v1 import enums
from cachetclient.v1.components import Component, ComponentManager
from cachetclient.httpclient import HttpClient


class CompontentGroup(Resource):

    @property
    def id(self) -> int:
        """int: Id of the component group"""
        return self.get('id')

    @property
    def name(self) -> str:
        """str: Set or get name of component group"""
        return self._data['name']

    @name.setter
    def name(self, value: str):
        self._data['name'] = value

    @property
    def enabled_components(self) -> List[Component]:
        """List[Component]: Enabled components in this group"""
        return [Component(self._manager.components, comp)
                for comp in self._data['enabled_components']]

    @property
    def order(self) -> int:
        """int: Get or set order value for group"""
        return self.get('order')

    @order.setter
    def order(self, value: int):
        self._data['order'] = value

    @property
    def collapsed(self) -> int:
        """int: Get or set collapsed status.
        See :py:data:`enums` module for values.
        """
        return self.get('collapsed')

    @collapsed.setter
    def collapsed(self, value):
        self._data['collapsed'] = value

    @property
    def lowest_human_status(self):
        """str: Lowest component status, human readable"""
        return self.get('lowest_human_status')

    @property
    def is_collapsed(self) -> bool:
        """bool: Does the current collapsed value indicate the group is collapsed?
        Note that the collapsed value may also indicate the group is not operational.
        """
        return self.collapsed == enums.COMPONENT_GROUP_COLLAPSED_TRUE

    @property
    def is_open(self) -> bool:
        """bool: Does the current collapsed value indicate the group is open?
        Note that the collapsed value may also indicate the group is not operational.
        """
        return self.collapsed == enums.COMPONENT_GROUP_COLLAPSED_FALSE

    @property
    def is_operational(self) -> bool:
        """bool: Does the current collapsed value indicate the group not operational?"""
        return self.collapsed != enums.COMPONENT_GROUP_COLLAPSED_NOT_OPERATIONAL

    @property
    def created_at(self) -> datetime:
        """datatime: When the group was created"""
        return utils.to_datetime(self.get('created_at'))

    @property
    def updated_at(self) -> datetime:
        """datetime: Last time updated"""
        return utils.to_datetime(self.get('updated_at'))


class CompontentGroupManager(Manager):
    resource_class = CompontentGroup
    path = 'components/groups'

    def __init__(self, http_client: HttpClient, components_manager: ComponentManager):
        super().__init__(http_client)
        self.components = components_manager

    def create(self, *, name: str, order: int = 0, collapsed: int = 0) -> CompontentGroup:
        """
        Create a component group

        Keyword Args:
            name (str): Name of the group
            order (int): group order
            collapsed (int): Collapse value (see enums)

        Returns:
            :py:data:`CompoentGroup` instance
        """
        return self._create(
            self.path,
            {
                'name': name,
                'order': order,
                'collapsed': collapsed,
            }
        )

    def update(self, group_id: int, *, name: str, order: int = None,
               collapsed: int = None, **kwargs) -> CompontentGroup:
        """
        Update component group

        Args:
            group_id (int): The group id to update

        Keyword Args:
            name (str): New name for group
            order (int): Order value of the group
            collapsed (int): Collapsed value. See enums module.
        """
        return self._update(
            self.path,
            group_id,
            self._build_data_dict(
                name=name,
                order=order,
                collapsed=collapsed,
            ),
        )

    def count(self) -> int:
        """
        Count the number of component groups

        Returns:
            int: Number of component groups
        """
        return self._count(self.path)

    def list(self, page: int = 1, per_page: int = 20) -> Generator[CompontentGroup, None, None]:
        """
        List all component groups

        Keyword Args:
            page (int): The page to start listing
            per_page: Number of entires per page

        Returns:
            Generator of :py:data:`ComponentGroup` instances
        """
        yield from self._list_paginated(self.path, page=page, per_page=per_page)

    def get(self, group_id) -> CompontentGroup:
        """
        Get a component group by id

        Args:
            group_id (int): Id of the component group

        Returns:
            :py:data:`ComponentGroup` instance

        Raises:
            `requests.exceptions.HttpError`: if not found
        """
        return self._get(self.path, group_id)

    def delete(self, group_id: int) -> None:
        """
        Delete a component group

        Args:
            group_id (int): Id of the component

        Raises:
            `requests.exceptions.HttpError`: if not found
        """
        self._delete(self.path, group_id)
