from datetime import datetime
from typing import Generator, List

from cachetclient.base import Manager, Resource
from cachetclient import utils


class Subscriber(Resource):

    @property
    def id(self) -> int:
        """int: Resource ID"""
        return int(self._data['id'])

    @property
    def email(self) -> str:
        """str: email address"""
        return self._data['email']

    @property
    def verify_code(self) -> str:
        """str: Auto generated unique verify code"""
        return self._data['verify_code']

    @property
    def is_global(self) -> bool:
        """bool: Is the user subscribed to all components?"""
        return self._data['global']

    @property
    def created_at(self) -> datetime:
        """datetime: When the subscription was created"""
        return utils.to_datetime(self.get('created_at'))

    @property
    def updated_at(self) -> datetime:
        """datetime: Last time the subscription was updated"""
        return utils.to_datetime(self.get('updated_at'))

    @property
    def verified_at(self) -> datetime:
        """datetime: When the subscription was verified. ``None`` if not verified"""
        return utils.to_datetime(self.get('verified_at'))

    def __str__(self) -> str:
        return "<Subscriber {}: {}>".format(self.id, self.email)


class SubscriberManager(Manager):
    """Manager for subscriber endpoints"""
    resource_class = Subscriber
    path = 'subscribers'

    def create(self, *, email: str, components: List[int] = None, verify: bool = True) -> Subscriber:
        """Create a subscriber.
        If a subscriber already exists the existing one will be returned.
        Note that this endoint cannot be used to edit the user.

        Keyword Args:
            email (str): Email address to subscribe
            components (List[int]): The components to subscribe to. If omitted all components are subscribed.
            verify (bool): Verification status. If ``False`` a verification email is sent to the user

        Returns:
            :py:data:`Subscriber` instance
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
        """List all subscribers

        Keyword Args:
            page (int): The page to start listing
            per_page: Number of entries per page

        Returns:
            Generator of Subscriber instances
        """
        yield from self._list_paginated(self.path, page=page, per_page=per_page)

    def delete(self, subscriber_id: int) -> None:
        """Delete a specific subscriber id

        Args:
            subscriber_id (int): Subscriber id to delete

        Raises:
            :py:data:`requests.exceptions.HttpError`: if subscriber do not exist
        """
        self._delete(self.path, subscriber_id)

    def count(self) -> int:
        """Count the total number of subscribers

        Returns:
            int: Number of subscribers
        """
        return self._count(self.path)
