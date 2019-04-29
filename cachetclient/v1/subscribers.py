from datetime import datetime
from typing import Generator

from cachetclient.base import Manager, Resource


class Subscriber(Resource):

    def __init__(self, manager, data):
        super().__init__(manager, data)

    @property
    def id(self) -> int:
        return int(self._data['id'])

    @property
    def email(self) -> str:
        return self._data['email']

    @property
    def verify_code(self) -> str:
        return self._data['verify_code']

    @property
    def verified_at(self) -> str:
        return self._data['verified_at']

    @property
    def is_global(self) -> bool:
        return self._data['global'] == 'true'

    @property
    def created_at(self) -> datetime:
        return self._data['created_at']

    @property
    def updated_at(self) -> datetime:
        return self._data['created_at']

    def __str__(self) -> str:
        return "<Subscriber {}: {}>".format(self.id, self.email)


class SubscriberManager(Manager):
    resource_class = Subscriber
    path = 'subscribers'

    def create_or_update(self, email, components=None, verify=True) -> Subscriber:
        """Create or update a subscriber"""
        self._http.post(
            self.path,
            data={
                'email': email,
                'components': components,
                'verify': verify,
            },
        )

    def list(self) -> Generator[Subscriber, None, None]:
        yield from self._list_paginated(self.path)

    def delete(self, subscriber_id) -> None:
        self._delete(self.path, subscriber_id)

    def count(self) -> int:
        return self._count(self.path)
