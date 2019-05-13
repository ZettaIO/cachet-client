from typing import Generator

from cachetclient.base import Manager, Resource


class CompontentGroup(Resource):

    @property
    def id(self) -> int:
        """Id of the component group"""
        return self._data['id']

    @property
    def name(self) -> str:
        """Name of component group"""
        return self._data['name']

    @name.setter
    def name(self, value):
        self._data['name'] = value

    @property
    def order(self) -> int:
        """Order value for group"""
        return self._data['order']

    @order.setter
    def order(self, value):
        self._data['order'] = value

    @property
    def collapsed(self) -> int:
        """
        Is the group collapsed?
        See enums module for values
        """
        return self._data['collapsed']

    @collapsed.setter
    def collapsed(self, value):
        self._data['collapsed'] = value

    @property
    def created_at(self):
        """Date/time created"""
        return self._data['created_at']

    @property
    def updated_at(self):
        """Date/time updated"""
        return self._data['updated_at']


class CompontentGroupManager(Manager):
    resource_class = CompontentGroup
    path = 'components/groups'

    def create(self, name, order=0, collapsed=0) -> CompontentGroup:
        """
        Create a component group

        Params:
            name (str): Name of the group
            order (int): group order
            collapsed (int): Collapse value (see enums)
        
        Return:
            CompoentGroup instance
        """
        return self._create(
            self.path,
            {
                'name': name,
                'order': order,
                'collapsed': collapsed,
            }
        )

    def update(self, group_id, name=None, order=None, collapsed=None, **kwargs):
        """
        Update component group

        Params:
            group_id (int): The group id to update
            name (str): New name for group
            order (int): Order value of the group
            collapsed (int): Collapsed value. See enums module.
        """
        return self._update(
            self.path,
            group_id,
            {
                'name': name,
                'order': order,
                'collapsed': collapsed,
            }
        )

    def count(self) -> int:
        """
        Count the number of component groups

        Returns:
            (int) Number of component groups
        """
        return self._count(self.path)

    def list(self, page: int = 1, per_page: int = 20) -> Generator[CompontentGroup, None, None]:
        """
        List all component groups

        Params:
            page (int): The page to start listing
            per_page: Number of entires per page

        Returns:
            Generator of ComponentGroup instances
        """
        yield from self._list_paginated(self.path, page=page, per_page=per_page)

    def get(self, group_id) -> CompontentGroup:
        """
        Get a component group by id

        Params:
            group_id (int): Id of the component group

        Returns:
            ComponentGroup instance
        
        Raises:
            HttpError if not found
        """
        return self._get(self.path, group_id)

    def delete(self, group_id: int) -> None:
        """
        Delete a component group

        Params:
            group_id (int): Id of the component

        Raises:
            HTTPError if compontent do not exist
        """
        self._delete(self.path, group_id)
