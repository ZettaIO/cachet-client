import logging
from cachetclient.base import Manager

logger = logging.getLogger(__name__)


class PingManager(Manager):
    path = 'ping'

    def __call__(self) -> bool:
        """Get version info"""
        return self.get()

    def get(self) -> bool:
        """Get version info"""
        # FIXME: Test more explicit exceptions
        try:
            response = self._http.get(self.path)
            data = response.json()
            return data['data'] == 'Pong!'
        except Exception as ex:
            logger.warning("Ping: %s", ex)
            return False

        return True
