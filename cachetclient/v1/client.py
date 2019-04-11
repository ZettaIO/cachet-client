from cachetclient.httpclient import HttpClient
from cachetclient.v1.component_groups import CompontentGroupManager
from cachetclient.v1.components import ComponentManager
from cachetclient.v1.incidents import IncidentManager
from cachetclient.v1.metrics import MetricsManager
from cachetclient.v1.subscribers import SubscriberManager


class Client:

    def __init__(self, http_client):
        """
        Args:
            http_client: The http client class to use
        """
        self._http = http_client

        # Managers
        self.component_groups = CompontentGroupManager(self._http)
        self.components = ComponentManager(self._http)
        self.incidents = IncidentManager(self._http)
        self.metrics = MetricsManager(self._http)
        self.subscribers = SubscriberManager(self._http)
