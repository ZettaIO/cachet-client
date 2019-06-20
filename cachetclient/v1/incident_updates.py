from datetime import datetime

from cachetclient.base import Manager, Resource
from cachetclient import utils


class IndicentUpdate(Resource):

    @property
    def id(self) -> int:
        return self.get('id')

    @property
    def incident_id(self) -> int:
        return self.get('incident_id')

    @property
    def status(self) -> int:
        return self.get('status')

    @status.setter
    def status(self, value: int):
        self._data['status'] = value

    @property
    def messages(self) -> str:
        return self.get('message')

    @messages.setter
    def message(self, value: str):
        self._data['message'] = value

    @property
    def user_id(self) -> int:
        return self.get('user_id')

    @property
    def created_at(self) -> datetime:
        return utils.to_datetime(self.get('created_at'))

    @property
    def updated_at(self) -> datetime:
        return utils.to_datetime(self.get('updated_at'))

    @property
    def human_status(self) -> str:
        return self.get('human_status')

    @property
    def permlink(self) -> str:
        """Permanent url"""
        return self.get('permlink')

    def update(self):
        """Update/save changes"""
        return self._manager.update(**self.attrs)

    def delete(self):
        self._manager.delete(self.incident_id, self.id)


class IncidentUpdatesManager(Manager):
    resource_class = IndicentUpdate
    path = 'incidents/{}/updates'

    def create(self, incident_id: int, status: int, message: str):
        """
        Create an incident update

        Args:
            incident_id (int): The incident to update
            status (int): New status id
            message (str): Update message

        Returns:
            IndicentUpdate instance
        """
        return self._create(
            self.path.format(incident_id),
            {
                'status': status,
                'message': message,
            }
        )

    def update(self, incident_id: int = None, id: int = None, status: int = None, message: str = None, **kwargs):
        """
        Update an incident update

        Args:
            incident_id (int): The incident
            id (int): The incident update id to update

        Keyword Args:
            status (int): New status id
            message (str): New message

        Returns:
            The updated IncidentUpdate instance
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

    def count(self, incident_id):
        """
        Count the number of indicent update for an issue

        Returns:
            (int) Number of incident updates for the issue
        """
        return self._count(self.path.format(incident_id))

    def list(self, incident_id: int, page=1, per_page=20):
        """
        List updates for an issue

        Args:
            incident_id: The incident to list updates

        Keyword Args:
            page (int): The first page to request
            per_page (int): Entires per page

        Return:
            Generator of incident updates
        """
        return self._list_paginated(
            self.path.format(incident_id),
            page=page,
            per_page=per_page,
        )

    def get(self, incident_id, update_id):
        """
        Get an incident update

        Args:
            incident_id (int): The incident
            update_id (int): The indicent update id to obtain

        Returns:
            IncidentUpdate instance
        """
        return self._get(self.path.format(incident_id), update_id)

    def delete(self, incident_id, update_id):
        """
        Delete an incident update
        """
        self._delete(self.path.format(incident_id), update_id)
