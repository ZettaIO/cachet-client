"""
Documentation testing

Inspired by: https://github.com/cprogrammer1994/ModernGL/blob/master/tests/test_documentation.py
by Szabolcs Dombi

This version is simplified:

* Only test if the attribute or method/function is present in the class. Parameters are not inspected.
* Include ignore pattern in the implemented set
"""
import os
import re
import types
import unittest
from importlib import import_module


class DocTestCase(unittest.TestCase):
    """
    Test reference docs
    """
    def validate(self, filename, module, classname=None, ignore=None):
        """
        Finds all automethod and autoattribute statements in an rst file
        comparing them to the attributes found in the actual class
        """
        if ignore is None:
            ignore = []

        with open(os.path.normpath(os.path.join('docs', 'reference', filename))) as f:
            docs = f.read()

        module = import_module(module)

        # Inspect class
        if classname:
            methods = re.findall(r'^\.\. automethod:: ([^\(\n]+)', docs, flags=re.M)
            attributes = re.findall(r'^\.\. autoattribute:: ([^\n]+)', docs, flags=re.M)

            documented = set(filter(lambda x: x.startswith(classname + '.'), [a for a in methods] + attributes))
            implemented = set(classname + '.' + x for x in dir(getattr(module, classname))
                              if not x.startswith('_') or x in ['__init__', '__call__'])
            ignored = set(classname + '.' + x for x in ignore)
        # Inspect module
        else:
            # Only inspect functions for now
            functions = re.findall(r'^\.\. autofunction:: ([^\(\n]+)', docs, flags=re.M)
            documented = set(functions)
            ignored = set(ignore)
            implemented = set(func for func in dir(module) if isinstance(getattr(module, func), types.FunctionType))

        self.assertSetEqual(implemented - documented - ignored, set(), msg='Implemented but not Documented')
        self.assertSetEqual(documented - implemented - ignored, set(), msg='Documented but not Implemented')

    def test_client(self):
        self.validate('cachetclient.client.rst', 'cachetclient.client', ignore=['detect_version'])

    def test_component_group(self):
        self.validate('cachetclient.v1.component_groups.rst', 'cachetclient.v1.component_groups', classname='ComponentGroup')

    def test_component_group_manager(self):
        self.validate('cachetclient.v1.component_groups.rst', 'cachetclient.v1.component_groups', classname='ComponentGroupManager')

    def test_component(self):
        self.validate('cachetclient.v1.components.rst', 'cachetclient.v1.components', classname='Component')

    def test_component_manager(self):
        self.validate('cachetclient.v1.components.rst', 'cachetclient.v1.components', classname='ComponentManager')

    def test_enums(self):
        self.validate('cachetclient.v1.enums.rst', 'cachetclient.v1.enums')

    def test_incident_update(self):
        self.validate('cachetclient.v1.incident_updates.rst', 'cachetclient.v1.incident_updates', classname='IncidentUpdate')

    def test_incident_update_manager(self):
        self.validate('cachetclient.v1.incident_updates.rst', 'cachetclient.v1.incident_updates', classname='IncidentUpdatesManager')

    def test_incident(self):
        self.validate('cachetclient.v1.incidents.rst', 'cachetclient.v1.incidents', classname='Incident')

    def test_incident_manager(self):
        self.validate('cachetclient.v1.incidents.rst', 'cachetclient.v1.incidents', classname='IncidentManager')

    def test_metric_points(self):
        self.validate('cachetclient.v1.metric_points.rst', 'cachetclient.v1.metric_points', classname='MetricPoint')

    def test_metric_points_manager(self):
        self.validate('cachetclient.v1.metric_points.rst', 'cachetclient.v1.metric_points', classname='MetricPointsManager')

    def test_metrics(self):
        self.validate('cachetclient.v1.metrics.rst', 'cachetclient.v1.metrics', classname='Metric')

    def test_metrics_manager(self):
        self.validate('cachetclient.v1.metrics.rst', 'cachetclient.v1.metrics', classname='MetricsManager')

    def test_ping(self):
        self.validate('cachetclient.v1.ping.rst', 'cachetclient.v1.ping', classname='PingManager', ignore=['instance_from_dict', 'instance_list_from_json', 'instance_from_json'])

    def test_subscribers(self):
        self.validate('cachetclient.v1.subscribers.rst', 'cachetclient.v1.subscribers', classname='Subscriber')

    def test_subscribers_manager(self):
        self.validate('cachetclient.v1.subscribers.rst', 'cachetclient.v1.subscribers', classname='SubscriberManager')

    def test_version(self):
        self.validate('cachetclient.v1.version.rst', 'cachetclient.v1.version', classname='Version', ignore=['delete', 'update'])

    def test_version(self):
        self.validate('cachetclient.v1.version.rst', 'cachetclient.v1.version', classname='VersionManager')
