from datetime import datetime

from cachetclient.base import Manager, Resource
from cachetclient.v1 import enums
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

    @property
    def messages(self) -> str:
        return self.get('message')

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


class IncidentUpdatesManager(Manager):
    resource_class = IndicentUpdate
    path = 'incidents/{resource_id}/updates'

    def create(self):
        """
        Create an incident update
        """
        pass

    def update(self):
        """
        Update an incident update
        """
        pass

    def list(self):
        """
        List updates for an issue
        """
        pass

    def get(self):
        """
        Get an incident update
        """
        pass

    def delete(self, incident_id, update_id):
        """
        Delete an incident update
        """
        pass
