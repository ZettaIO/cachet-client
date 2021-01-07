import logging
from cachetclient.base import Manager

logger = logging.getLogger(__name__)


class PingManager(Manager):
    """Manager for ping endpoints"""

    path = "ping"

    def __call__(self) -> bool:
        """
        Shortcut for the :py:data:`get` method.

        Example::

            >> client.ping()
            True
        """
        return self.get()

    def get(self) -> bool:
        """
        Check if the cachet api is responding.

        Example::

            >> client.ping.get()
            True

        Returns:
            bool: ``True`` if a successful response. Otherwise ``False``.
        """
        # FIXME: Test more explicit exceptions
        try:
            response = self._http.get(self.path)
            data = response.json()
            return data["data"] == "Pong!"
        except Exception as ex:
            logger.warning("Ping: %s", ex)
            return False
