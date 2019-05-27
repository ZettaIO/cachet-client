from cachetclient.base import Manager


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
            print(ex)
            return False

        return True
