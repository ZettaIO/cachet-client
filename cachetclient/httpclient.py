from urllib.parse import urljoin

import requests


class HttpClient:

    def __init__(self, base_url, api_token, verify_tls=True):
        self.base_url = base_url
        self.verify_tls = verify_tls
        if not self.base_url.endswith('/'):
            self.base_url += '/'

        self._session = requests.Session()
        self._session.headers.update({'X-Cachet-Token': api_token})

    def get(self, path):
        return self.request('GET', path)

    def post(self, path):
        return self.request('POST', path)

    def delete(self, path):
        return self.request('DELETE', path)

    def request(self, method, path, params=None, data=None):
        url = urljoin(self.base_url, path)
        result = self._session.request(
            method,
            url,
            params=params,
            data=None,
            verify=self.verify_tls,
        )
        if result.ok:
            return result

        result.raise_for_status()
