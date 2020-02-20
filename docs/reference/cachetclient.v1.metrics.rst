.. py:module:: cachetclient.v1.metrics
.. py:currentmodule:: cachetclient.v1.metrics

Metrics
=======

Resource
--------

Methods
*******

.. automethod:: Metric.__init__
.. automethod:: Metric.get
.. automethod:: Metric.delete
.. automethod:: Metric.update

Attributes
**********

.. autoattribute:: Metric.attrs
.. autoattribute:: Metric.id
.. autoattribute:: Metric.name
.. autoattribute:: Metric.description
.. autoattribute:: Metric.default_value
.. autoattribute:: Metric.display_chart
.. autoattribute:: Metric.places
.. autoattribute:: Metric.points
.. autoattribute:: Metric.threshold
.. autoattribute:: Metric.visible
.. autoattribute:: Metric.order
.. autoattribute:: Metric.suffix
.. autoattribute:: Metric.calc_type
.. autoattribute:: Metric.default_view
.. autoattribute:: Metric.created_at
.. autoattribute:: Metric.updated_at

Manager
-------

Methods
*******

.. automethod:: MetricPointsManager.__init__
.. automethod:: MetricPointsManager.create
.. automethod:: MetricPointsManager.list
.. automethod:: MetricPointsManager.count
.. automethod:: MetricPointsManager.delete
.. automethod:: MetricPointsManager.instance_from_dict
.. automethod:: MetricPointsManager.instance_from_json
.. automethod:: MetricPointsManager.instance_list_from_json

Attributes
**********

.. autoattribute:: MetricPointsManager.path
.. autoattribute:: MetricPointsManager.resource_class
