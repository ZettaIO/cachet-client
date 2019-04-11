from cachetclient.base import Manager, Resource


class IndicentUpdate(Resource):
    pass


class IncidentUpdatesManager(Manager):
    resource_class = IndicentUpdate
    path = 'incidents/{resource_id}/updates'
