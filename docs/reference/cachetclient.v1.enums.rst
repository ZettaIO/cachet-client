.. py:module:: cachetclient.v1.enums
.. py:currentmodule:: cachetclient.v1.enums

enums
=====

Constants / enums for various resources in cachet
like component and incident status value.

Component Status
----------------

.. autodata:: COMPONENT_STATUS_OPERATIONAL
   :annotation:
.. autodata:: COMPONENT_STATUS_PERFORMANCE_ISSUES
   :annotation:
.. autodata:: COMPONENT_STATUS_PARTIAL_OUTAGE
   :annotation:
.. autodata:: COMPONENT_STATUS_MAJOR_OUTAGE
   :annotation:
.. autodata:: COMPONENT_STATUS_LIST
   :annotation:

Component Group Collapsed
-------------------------

.. autodata:: COMPONENT_GROUP_COLLAPSED_FALSE
   :annotation:
.. autodata:: COMPONENT_GROUP_COLLAPSED_TRUE
   :annotation:
.. autodata:: COMPONENT_GROUP_COLLAPSED_NOT_OPERATIONAL
   :annotation:

Incident Status
---------------

.. autodata:: INCIDENT_SCHEDULED
   :annotation:
.. autodata:: INCIDENT_INVESTIGATING
   :annotation:
.. autodata:: INCIDENT_IDENTIFIED
   :annotation:
.. autodata:: INCIDENT_WATCHING
   :annotation:
.. autodata:: INCIDENT_FIXED
   :annotation:
.. autofunction:: incident_status_human

Schedule Status
---------------

.. autodata:: SCHEDULE_STATUS_UPCOMING
   :annotation:
.. autodata:: SCHEDULE_STATUS_IN_PROGRESS
   :annotation:
.. autodata:: SCHEDULE_STATUS_COMPLETE
   :annotation:
