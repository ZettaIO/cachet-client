from datetime import datetime
from typing import Generator, List

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
    def is_global(self) -> bool:
        return self._data['global']

    @property
    def created_at(self) -> datetime:
        return self._data['created_at']

    @property
    def updated_at(self) -> datetime:
        return self._data['created_at']

    @property
    def verified_at(self) -> str:
        return self._data['verified_at']

    def __str__(self) -> str:
        return "<Subscriber {}: {}>".format(self.id, self.email)


class SubscriberManager(Manager):
    resource_class = Subscriber
    path = 'subscribers'

    def create(self, email: str, components: List[int] = None, verify: bool = True) -> Subscriber:
        """
        Create or update a subscriber

        Params:
            email (str): Email address to subscribe
            components (int list): The components to subscribe to. If ommited all components are subscribed.
                        If no components are supplied the user will subscribe to all componets.
            verify (bool): Verification status. If False an verfication email is sent.

        Returns:
            The created or updated Subsriber instance
        """
        return self._create(
            self.path,
            {
                'email': email,
                'components': components,
                'verify': verify,
            },
        )

    def list(self, page: int = 1, per_page: int = 20) -> Generator[Subscriber, None, None]:
        """
        List all subscribers

        Params:
            page (int): The page to start listing
            per_page: Number of entires per page

        Returns:
            Generator of Subscriber instances
        """
        yield from self._list_paginated(self.path, page=page, per_page=per_page)

    def delete(self, subscriber_id) -> None:
        """
        Delete a specific subscriber id

        Returns:
            None or raises exception
        """
        self._delete(self.path, subscriber_id)

    def count(self) -> int:
        """
        Count the total number of subscribers

        Returns:
            (int) number of subscribers
        """
        return self._count(self.path)
