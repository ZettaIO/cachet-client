from cachetclient.base import Manager, Resource


class Incident(Resource):
    pass


class IncidentManager(Manager):
    resource_class = Incident
