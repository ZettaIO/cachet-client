.. py:module:: cachetclient.v1.schedules
.. py:currentmodule:: cachetclient.v1.schedules

Schedules
=========

Resource
--------

Methods
*******

.. automethod:: Schedule.get
.. automethod:: Schedule.update
.. automethod:: Schedule.delete

Attributes
**********

.. autoattribute:: Schedule.id
.. autoattribute:: Schedule.name
.. autoattribute:: Schedule.message
.. autoattribute:: Schedule.status
.. autoattribute:: Schedule.scheduled_at
.. autoattribute:: Schedule.completed_at
.. autoattribute:: Schedule.attrs

Manager
-------

Methods
*******

.. automethod:: ScheduleManager.__init__
.. automethod:: ScheduleManager.create
.. automethod:: ScheduleManager.update
.. automethod:: ScheduleManager.list
.. automethod:: ScheduleManager.get
.. automethod:: ScheduleManager.delete
.. automethod:: ScheduleManager.instance_from_dict
.. automethod:: ScheduleManager.instance_from_json
.. automethod:: ScheduleManager.instance_list_from_json

Attributes
**********

.. autoattribute:: ScheduleManager.path
.. autoattribute:: ScheduleManager.resource_class
