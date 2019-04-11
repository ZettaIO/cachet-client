from cachetclient.base import Manager, Resource


class Component(Resource):
    pass


class ComponentManager(Manager):
    resource_class = Component
