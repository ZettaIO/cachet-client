from datetime import datetime
from typing import List

from cachetclient.base import Manager, Resource
from cachetclient.v1 import enums
from cachetclient import utils


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
        return self.get('visible')

    @property
    def message(self) -> str:
        """(str) Indicent body message"""
        return self.get('message')

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


class IncidentManager(Manager):
    resource_class = Incident
    path = 'incidents'


    def create(
            self,
            name: str,
            message: str,
            status: int,
            visible: int,
            component_id: int = None,
            component_status: int = None,
            notify: bool = None,
            created_at: datetime = None,
            template: str = None,
            template_vars: List[str] = None):
        """
        """
        return self._create(
            self.path,
            {
                'name': name,
                'message': message,
                'status': status,
                'visible': visible,
                'component_id': component_id,
                'component_status': component_status,
                'notify': notify,
                'created_at': created_at,
                'template': template,
                'vars': template_vars,
            }
        )

    def update(self):
        pass

    def list(self):
        pass

    def delete(self):
        pass
