.. py:module:: cachetclient.v1.incidents
.. py:currentmodule:: cachetclient.v1.incidents

Incidents
=========

Resource
--------

Methods
*******

.. automethod:: Incident.__init__
.. automethod:: Incident.updates
.. automethod:: Incident.update
.. automethod:: Incident.get
.. automethod:: Incident.delete

Attributes
**********

.. autoattribute:: Incident.attrs
.. autoattribute:: Incident.id
.. autoattribute:: Incident.component_id
.. autoattribute:: Incident.name
.. autoattribute:: Incident.message
.. autoattribute:: Incident.notify
.. autoattribute:: Incident.status
.. autoattribute:: Incident.human_status
.. autoattribute:: Incident.visible
.. autoattribute:: Incident.scheduled_at
.. autoattribute:: Incident.created_at
.. autoattribute:: Incident.updated_at
.. autoattribute:: Incident.deleted_at

Manager
-------

Methods
*******

.. automethod:: IncidentManager.__init__
.. automethod:: IncidentManager.create
.. automethod:: IncidentManager.update
.. automethod:: IncidentManager.list
.. automethod:: IncidentManager.get
.. automethod:: IncidentManager.count
.. automethod:: IncidentManager.delete
.. automethod:: IncidentManager.instance_from_dict
.. automethod:: IncidentManager.instance_from_json
.. automethod:: IncidentManager.instance_list_from_json

Attributes
**********

.. autoattribute:: IncidentManager.path
.. autoattribute:: IncidentManager.resource_class
