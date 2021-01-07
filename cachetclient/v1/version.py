from cachetclient.base import Manager, Resource


class Version(Resource):
    @property
    def value(self) -> str:
        """str: Version string from Cachet service"""
        return self._data["data"]

    @property
    def on_latest(self) -> bool:
        """bool: Are we on latest version?
        Requires beacon enabled on server.
        """
        return self._data["meta"]["on_latest"]

    @property
    def latest(self) -> dict:
        """dict: Obtains info dict about latest version.
        Requires beacon enabled on server.

        Dict format is::

            {
                "tag_name": "v2.3.10",
                "prelease": false,
                "draft": false
            }

        """
        return self._data["meta"]["latest"]


class VersionManager(Manager):
    resource_class = Version
    path = "version"

    def __call__(self) -> Version:
        """Shortcut to :py:data:`get`

        Example::

            >> version = client.version()
            >> version.value
            v2.3.10
        """
        return self.get()

    def get(self) -> Version:
        """Get version info from the server

        Example::

            >> version = client.version.get()
            >> version.value
            v2.3.10

        Returns:
            :py:data:`Version` instance
        """
        response = self._http.get(self.path)
        return Version(self, response.json())
