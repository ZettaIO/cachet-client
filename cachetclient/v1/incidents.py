from datetime import datetime
from typing import List

from cachetclient.base import Manager, Resource
from cachetclient.v1 import enums
from cachetclient import utils
from cachetclient.v1.incident_updates import IncidentUpdatesManager
from cachetclient.httpclient import HttpClient


class Incident(Resource):

    @property
    def id(self) -> int:
        """(int) The unique id for the incident"""
        return self.get('id')

    @property
    def component_id(self) -> int:
        """(int) The component id for this incident"""
        return self.get('component_id')

    @property
    def name(self) -> str:
        """(str) Name/title of the incident"""
        return self.get('name')

    @property
    def message(self) -> str:
        """(str) Indicent body message"""
        return self.get('message')

    @property
    def notify(self) -> str:
        """(bool) Notify user"""
        return self.get('notify')

    @property
    def status(self) -> int:
        """(int) Status of the incident"""
        return self.get('status')

    @property
    def human_status(self) -> str:
        """(str) Human representation of the status"""
        return self.get('human_status')

    @property
    def visible(self) -> int:
        """(int) Visibility of the indcinent"""
        return self.get('visible') == 1

    @property
    def scheduled_at(self) -> datetime:
        return utils.to_datetime(self.get('scheduled_at'))

    @property
    def created_at(self) -> datetime:
        """(datetime) When the issue was created"""
        return utils.to_datetime(self.get('created_at'))

    @property
    def updated_at(self) -> datetime:
        """(datetime) Last time the issue was updated"""
        return utils.to_datetime(self.get('updated_at'))

    @property
    def deleted_at(self) -> datetime:
        """(datetime) When the issue was deleted"""
        return utils.to_datetime(self.get('deleted_at'))

    def updates(self):
        """Get incident updates for this issue"""
        return self._manager.updates.list(self.id)


class IncidentManager(Manager):
    resource_class = Incident
    path = 'incidents'

    def __init__(self, http_client: HttpClient, incident_update_manager: IncidentUpdatesManager):
        super().__init__(http_client)
        self.updates = incident_update_manager

    def create(
            self,
            name: str,
            message: str,
            status: int,
            visible: bool = True,
            component_id: int = None,
            component_status: int = None,
            notify: bool = True,
            created_at: datetime = None,
            template: str = None,
            template_vars: List[str] = None):
        """
        Create and general issue or issue for a component.
        component_id and component_status must be supplied when making
        a component issue.

        Args:
            name (str): Name/title of the issue
            message (str): Mesage body for the issue
            status (int): Status of the incident (see enums)

        Keyword Args:
            visible (bool): Publicly visible incident
            component_id (int): The component to update
            component_status (int): The status to apply on component
            notify (bool): If users should be notified
            created_at: when the indicent was created
            template (str): Slug of template to use
            template_vars (list): Variables to the template
        """
        return self._create(
            self.path,
            {
                'name': name,
                'message': message,
                'status': status,
                'visible': 1 if visible else 0,
                'component_id': component_id,
                'component_status': component_status,
                'notify': 1 if notify else 0,
                'created_at': created_at,
                'template': template,
                'vars': template_vars,
            }
        )

    def update(self):
        pass

    def list(self):
        pass

    def delete(self, incident_id):
        """
        Delete an incident

        Args:
            incident_id (int): The incident id
        """
        self._delete(self.path, incident_id)
