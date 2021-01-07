from typing import (
    Any,
    Dict,
)
import logging
from urllib.parse import urljoin

import requests

logger = logging.getLogger(__name__)


class HttpClient:
    def __init__(
        self,
        base_url: str,
        api_token: str,
        timeout: float = None,
        verify_tls: bool = True,
        user_agent: str = None,
    ):

        self.base_url = base_url
        if not self.base_url.endswith("/"):
            self.base_url += "/"
        self.verify_tls = verify_tls
        self.timeout = timeout
        self.user_agent = user_agent

        self._session = requests.Session()
        self._session.headers.update(
            {
                "X-Cachet-Token": api_token,
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )
        if user_agent:
            self._session.headers.update({"User-Agent": user_agent})

    def get(self, path, params=None) -> requests.Response:
        return self.request("GET", path, params=params)

    def post(self, path, data) -> requests.Response:
        return self.request("POST", path, data=data)

    def put(self, path, data) -> requests.Response:
        return self.request("PUT", path, data=data)

    def delete(self, path, resource_id) -> requests.Response:
        return self.request("DELETE", "{}/{}".format(path, resource_id))

    def request(
        self,
        method: str,
        path: str,
        params: Dict[str, Any] = None,
        data: Dict[str, Any] = None,
    ) -> requests.Response:
        url = urljoin(self.base_url, path)
        response = self._session.request(
            method,
            url,
            params=params,
            json=data,
            verify=self.verify_tls,
            timeout=self.timeout,
        )
        logger.debug("%s %s", method, response.url)
        if response.ok:
            return response

        logger.debug(response.text)
        response.raise_for_status()
        raise RuntimeError
