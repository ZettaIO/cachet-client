from cachetclient.base import Manager, Resource


class PingManager(Manager):
    path = 'ping'

    def __call__(self):
        """Get version info"""
        return self.get()

    def get(self):
        """Get version info"""
        try:
            response = self._http.get(self.path)
            data = response.json()
            return data['data'] == 'Pong!'
        except Exception as ex:
            print(ex)
            return False

        return True
