from cachetclient.base import Manager, Resource


class Metrics(Resource):

    @property
    def id(self) -> int:
        return self.get('id')

    @property
    def name(self) -> str:
        return self.get('name')

    @property
    def suffix(self) -> str:
        return self.get('suffix')

    @property
    def description(self):
        return self.get('description')

    @property
    def default_value(self):
        return self.get('default_value')

    @property
    def calc_type(self) -> int:
        return self.get('calc_type')

    @property
    def display_chart(self) -> int:
        return self.get('display_chart')

    @property
    def created_at(self):
        self.get('created_at')

    @property
    def updated_at(self):
        self.get('updated_at')

    @property
    def default_view_name(self):
        return self.get('default_view_name')


class MetricsManager(Manager):
    resource_class = Metrics
    path = 'metrics'

    def create(self):
        pass

    def list(self, page: int = 1, per_page: int = 20):
        """
        List all metrics

        Keyword Args:
            page (int): Page to start listing
            per_page (int): Number of entries per page

        Returns:
            Generator of Metrics instances
        """
        return self._list_paginated(
            self.path,
            page=page,
            per_page=per_page,
        )

    def get(self):
        pass

    def delete(self, metrics_id):
        self._delete(self.path, metrics_id)
