from datetime import datetime
from typing import Generator

from cachetclient.base import Manager, Resource
from cachetclient import utils


class IndicentUpdate(Resource):

    @property
    def id(self) -> int:
        """int: Resource id"""
        return self.get('id')

    @property
    def incident_id(self) -> int:
        """int: The incident id this update belongs to"""
        return self.get('incident_id')

    @property
    def status(self) -> int:
        """int: Get or set incident status. See :py:data:`enums`."""
        return self.get('status')

    @status.setter
    def status(self, value: int):
        self._data['status'] = value

    @property
    def messages(self) -> str:
        """str: Get or set message"""
        return self.get('message')

    @messages.setter
    def message(self, value: str):
        self._data['message'] = value

    @property
    def user_id(self) -> int:
        """int: The user id creating the update"""
        return self.get('user_id')

    @property
    def created_at(self) -> datetime:
        """datetime: when the resource was created"""
        return utils.to_datetime(self.get('created_at'))

    @property
    def updated_at(self) -> datetime:
        """datetime: When the resource as last updated"""
        return utils.to_datetime(self.get('updated_at'))

    @property
    def human_status(self) -> str:
        """str: Human readable status"""
        return self.get('human_status')

    @property
    def permlink(self) -> str:
        """str: Permanent url to the incident update"""
        return self.get('permalink')

    def update(self) -> 'IndicentUpdate':
        """
        Update/save changes

        Returns:
            Updated IncidentUpdate instance
        """
        return self._manager.update(**self.attrs)

    def delete(self) -> None:
        """Deletes the incident update"""
        self._manager.delete(self.incident_id, self.id)


class IncidentUpdatesManager(Manager):
    resource_class = IndicentUpdate
    path = 'incidents/{}/updates'

    def create(self, *, incident_id: int, status: int, message: str) -> IndicentUpdate:
        """
        Create an incident update

        Keyword Args:
            incident_id (int): The incident to update
            status (int): New status id
            message (str): Update message

        Returns:
            :py:data:`IndicentUpdate` instance
        """
        return self._create(
            self.path.format(incident_id),
            {
                'status': status,
                'message': message,
            }
        )

    def update(
            self,
            *,
            id: int,
            incident_id: int,
            status: int = None,
            message: str = None,
            **kwargs) -> IndicentUpdate:
        """
        Update an incident update

        Args:
            incident_id (int): The incident
            id (int): The incident update id to update

        Keyword Args:
            status (int): New status id
            message (str): New message

        Returns:
            The updated :py:data:`IncidentUpdate` instance
        """
        # TODO: Documentation claims data is set as query params
        return self._update(
            self.path.format(incident_id),
            id,
            {
                'status': status,
                'message': message,
            }
        )

    def count(self, incident_id) -> int:
        """
        Count the number of indicent update for an incident

        Args:
            incident_id (int): The incident

        Returns:
            int: Number of incident updates for the incident
        """
        return self._count(self.path.format(incident_id))

    def list(self, incident_id: int, page: int = 1, per_page: int = 20) -> Generator[IndicentUpdate, None, None]:
        """
        List updates for an issue

        Args:
            incident_id: The incident to list updates

        Keyword Args:
            page (int): The first page to request
            per_page (int): Entries per page

        Return:
            Generator of :py:data:`IncidentUpdate`s
        """
        return self._list_paginated(
            self.path.format(incident_id),
            page=page,
            per_page=per_page,
        )

    def get(self, incident_id: int, update_id: int) -> IndicentUpdate:
        """
        Get an incident update

        Args:
            incident_id (int): The incident
            update_id (int): The indicent update id to obtain

        Returns:
            :py:data:`IncidentUpdate` instance
        """
        return self._get(self.path.format(incident_id), update_id)

    def delete(self, incident_id: int, update_id: int) -> None:
        """
        Delete an incident update
        """
        self._delete(self.path.format(incident_id), update_id)
