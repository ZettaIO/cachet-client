
Basic Usage
===========

Creating a client
-----------------

.. code:: python

    import cachetclient

    client = cachetclient.Client(
        endpoint='https://status.test/api/v1',
        api_token='secrettoken',
    )

Add a new subscriber with email verification
--------------------------------------------

.. code:: python

    sub = client.subscribers.create(email='user@example.test', verify=False)

List subscribers paginated
--------------------------

.. code:: python

    # Pagination under the hood scaling better with large numbers of subscribers
    for sub in client.subscribers.list(page=1, per_page=100):
        print(sub.id, sub.email, sub.verify_code)

Creating a component issue
--------------------------

.. code:: python

    from cachetclient.v1 import enums

    # Issue signaling to a component there is a major outage
    client.incidents.create(
        name="Something blew up!",
        message="We are looking into it",
        status=enums.INCIDENT_INVESTIGATING,
        component_id=1,
        component_status=enums.COMPONENT_STATUS_MAJOR_OUTAGE,
    )

Creating component group with components
----------------------------------------

.. code:: python

    from cachetclient.v1 import enums

    group = client.component_groups.create(name="Global Services")
    component = client.components.create(
        name="Public webside",
        status=enums.COMPONENT_STATUS_OPERATIONAL,
        description="This is a test",
        tags="test, web, something",
        group_id=group.id,
    )

Recreating resource from json or dict
-------------------------------------

Every manager has a method for recreating a resource
instance from a json string or dictionary. This can be
useful if data from cachet is cached or stored somewhere
like memcache or a database.

.. code:: python

    subscriber = client.subscribers.instance_from_json(json_str)
    subscriber = client.subscribers.instance_from_dict(data_dict)
