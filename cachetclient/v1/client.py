from cachetclient.httpclient import HttpClient
from cachetclient.v1.component_groups import ComponentGroupManager
from cachetclient.v1.components import ComponentManager
from cachetclient.v1.incidents import IncidentManager
from cachetclient.v1.incident_updates import IncidentUpdatesManager
from cachetclient.v1.metrics import MetricsManager
from cachetclient.v1.subscribers import SubscriberManager
from cachetclient.v1.ping import PingManager
from cachetclient.v1.version import VersionManager
from cachetclient.v1.schedules import ScheduleManager


class Client:

    def __init__(self, http_client: HttpClient):
        """
        Args:
            http_client: The http client class to use
        """
        self._http = http_client

        # Managers
        self.ping = PingManager(self._http)
        self.version = VersionManager(self._http)
        self.components = ComponentManager(self._http)
        self.component_groups = ComponentGroupManager(self._http, self.components)
        self.incident_updates = IncidentUpdatesManager(self._http)
        self.incidents = IncidentManager(self._http, self.incident_updates)
        self.metrics = MetricsManager(self._http)
        self.subscribers = SubscriberManager(self._http)
        self.schedules = ScheduleManager(self._http)
