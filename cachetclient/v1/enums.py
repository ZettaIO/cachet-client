# Component statuses
# 1 Operational 
# The component is working.
COMPONENT_STATUS_OPERATIONAL = 1
# 2 Performance Issues
# The component is experiencing some slowness.
COMPONENT_STATUS_PERFORMANCE_ISSUES = 2
# 3 Partial Outage
# The component may not be working for everybody. This could be a geographical issue for example.
COMPONENT_STATUS_PARTIAL_OUTAGE = 3
# 4 Major Outage
# The component is not working for anybody.
COMPONENT_STATUS_MAJOR_OUTAGE = 4

COMPONENT_STATUS_LIST = [
    COMPONENT_STATUS_OPERATIONAL,
    COMPONENT_STATUS_PERFORMANCE_ISSUES,
    COMPONENT_STATUS_PARTIAL_OUTAGE,
    COMPONENT_STATUS_MAJOR_OUTAGE
]

# Componet group collapse value
# 0 = No. 1 = Yes. 2 = If a component is not Operational.
COMPONENT_GROUP_COLLAPSED_FALSE = 0
COMPONENT_GROUP_COLLAPSED_TRUE = 1
COMPONENT_GROUP_COLLAPSED_NOT_OPERATIONAL = 2

# Incident Status
# 0 Scheduled
# This status is reserved for a scheduled status.
INCIDENT_SCHEDULED = 0
# 1 Investigating
# You have reports of a problem and you're currently looking into them.
INCIDENT_INVESTIGATING = 1
# 2 Identified
# You've found the issue and you're working on a fix.
INCIDENT_IDENTIFIED = 2
# 3 Watching
# You've since deployed a fix and you're currently watching the situation.
INCIDENT_WATCHING = 3
# 4 Fixed
# The fix has worked, you're happy to close the incident.
INCIDENT_FIXED = 4

SCHEDULE_STATUS_UPCOMING = 0
SCHEDULE_STATUS_IN_PROGRESS = 1
SCHEDULE_STATUS_COMPLETE = 2
