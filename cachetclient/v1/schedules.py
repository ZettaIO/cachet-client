from datetime import datetime

from cachetclient.base import Resource, Manager
from cachetclient.v1 import enums
from cachetclient import utils


class Schedule(Resource):

    @property
    def id(self) -> int:
        return self.get('id')

    @property
    def message(self) -> str:
        return self.get('message')

    @property
    def status(self) -> int:
        return self.get('status')

    @property
    def scheduled_at(self) -> datetime:
        return utils.to_datetime(self.get('scheduled_at'))

    @property
    def completed_at(self) -> datetime:
        return utils.to_datetime(self.get('completed_at'))


class ScheduleManager(Manager):
    path = 'schedules'
    resource_class = Schedule

    def create(self, *args, **kwargs):
        raise NotImplementedError()

    def update(self, *args, **kwargs):
        raise NotImplementedError()

    def list(self, *args, **kwargs):
        raise NotImplementedError()

    def delete(self, schedule_id):
        raise NotImplementedError()
