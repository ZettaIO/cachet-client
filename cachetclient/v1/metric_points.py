from cachetclient.base import Manager, Resource


class MetricPoints(Resource):
    pass


class MetricPointsManager(Manager):
    resource_class = MetricPoints
    path = 'metrics/{resource_id}/points'
