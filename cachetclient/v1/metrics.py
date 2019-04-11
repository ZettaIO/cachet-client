from cachetclient.base import Manager, Resource


class Metrics(Resource):
    pass


class MetricsManager(Manager):
    resource_class = Metrics
