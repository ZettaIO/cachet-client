import json
from urllib.parse import urljoin

import requests


class HttpClient:

    def __init__(self, base_url, api_token, timeout=None, verify_tls=True, user_agent=None):
        self.base_url = base_url
        if not self.base_url.endswith('/'):
            self.base_url += '/'
        self.verify_tls = verify_tls
        self.timeout = timeout
        self.user_agent = user_agent

        self._session = requests.Session()
        self._session.headers.update({
            'X-Cachet-Token': api_token,
            'User-Agent': user_agent,
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        })

    def get(self, path, params=None):
        return self.request('GET', path, params=params)

    def post(self, path, data):
        return self.request('POST', path, data=data)

    def delete(self, path):
        return self.request('DELETE', path)

    def request(self, method, path, params=None, data=None):
        url = urljoin(self.base_url, path)
        response = self._session.request(
            method,
            url,
            params=params,
            data=json.dumps(data),
            verify=self.verify_tls,
            timeout=self.timeout,
        )
        if response.ok:
            return response

        print(response.text)
        response.raise_for_status()
