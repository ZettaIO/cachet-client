# Component statuses
#: [1] Operational. The component is working.
COMPONENT_STATUS_OPERATIONAL = 1
#: [2] Performance Issues. The component is experiencing some slowness.
COMPONENT_STATUS_PERFORMANCE_ISSUES = 2
#: [3] Partial Outage. The component may not be working for everybody. This could be a geographical issue for example.
COMPONENT_STATUS_PARTIAL_OUTAGE = 3
#: [4] Major Outage. The component is not working for anybody.
COMPONENT_STATUS_MAJOR_OUTAGE = 4

#: List of all component statuses
#:
#: Can be used for::
#:
#:    >> status in enums.COMPONENT_STATUS_LIST
#:    True
COMPONENT_STATUS_LIST = [
    COMPONENT_STATUS_OPERATIONAL,
    COMPONENT_STATUS_PERFORMANCE_ISSUES,
    COMPONENT_STATUS_PARTIAL_OUTAGE,
    COMPONENT_STATUS_MAJOR_OUTAGE
]

# Component group collapse value
#: [0] No
COMPONENT_GROUP_COLLAPSED_FALSE = 0
#: [1] Yes
COMPONENT_GROUP_COLLAPSED_TRUE = 1
#: [2] Component is not Operational
COMPONENT_GROUP_COLLAPSED_NOT_OPERATIONAL = 2

# Incident Status
#: [0] Scheduled. This status is reserved for a scheduled status.
INCIDENT_SCHEDULED = 0
#: [1] Investigating. You have reports of a problem and you're currently looking into them.
INCIDENT_INVESTIGATING = 1
#: [2] Identified. You've found the issue and you're working on a fix.
INCIDENT_IDENTIFIED = 2
#: [3] Watching. You've since deployed a fix and you're currently watching the situation.
INCIDENT_WATCHING = 3
#: [4] Fixed. The fix has worked, you're happy to close the incident.
INCIDENT_FIXED = 4


def incident_status_human(status: int):
    """Get human status from incident status id

    Example::

        >> incident_status_human(enums.INCIDENT_FIXED)
        Fixed

    Args:
        status (int): Incident status id

    Returns:
        str: Human status
    """
    data = {
        INCIDENT_SCHEDULED: "Scheduled",
        INCIDENT_INVESTIGATING: "Investigating",
        INCIDENT_IDENTIFIED: "Identified",
        INCIDENT_WATCHING: "Watching",
        INCIDENT_FIXED: "Fixed",
    }
    return data[status]


# Schedule Status
#: [0] Upcoming
SCHEDULE_STATUS_UPCOMING = 0
#: [1] In progress
SCHEDULE_STATUS_IN_PROGRESS = 1
#: [2] Completed
SCHEDULE_STATUS_COMPLETE = 2
