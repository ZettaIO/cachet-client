[![pypi](https://badge.fury.io/py/cachet-client.svg)](https://pypi.python.org/pypi/cachet-client)
[![travis](https://api.travis-ci.org/ZettaIO/cachet-client.svg?branch=master)](https://travis-ci.org/ZettaIO/cachet-client) [![Documentation Status](https://readthedocs.org/projects/cachet-client/badge/?version=latest&nop)](https://cachet-client.readthedocs.io/en/latest/?badge=latest)

# cachet-client

A python 3.6+ API client for the open source status page system
[Cachet](https://github.com/CachetHQ/Cachet).

* [cachet-client on github](https://github.com/ZettaIO/cachet-client)
* [cachet-client on PyPI](https://pypi.org/project/cachet-client/)
* [cachet-client documentation](https://cachet-client.readthedocs.io/)

The goal of this package is to create a user friendly interface
to the Cachet API.

* Resources are returned as objects clearly separating read only
  properties from the ones we can change. The raw json response
  is always available in an `attrs` property
* Active use of type hints throughout the entire codebase
  making code completion a breeze
* Proper pagination under the hood. Method listing resources
  will return generators. You can configure the start page and
  page size that fits the situation. Each new page leads to
  a new http request.
* Client is using a single session regardless of resource type
  making more complex work a lot faster (connection reuse)
* A very extensive set of tests/unit tests.
* Easy to extend and test
* Documentation

**Please don't hesitate opening an issue about anything related to this package.**

## Install

```
pip install cachet-client
```

# Example

```python
import cachetclient
from cachetclient.v1 import enums

client = cachetclient.Client(
    endpoint='https://status.test/api/v1',
    api_token='secrettoken',
)
```

Check if api is responding

```python
if client.ping():
    print("Cachet is up and running!")
```

Create and delete a subscriber

```python
sub = client.subscribers.create(email='user@example.test', verify=True)
sub.delete()
```

List all subscribers paginated (generator). Each new page is fetched
from the server under the hood.

```python
for sub in client.subscribers.list(page=1, per_page=100):
    print(sub.id, sub.email)
```

Create a component issue

```python
issue = client.incidents.create(
    name="Something blew up!",
    message="We are looking into it",
    status=enums.INCIDENT_INVESTIGATING,
    # Optional for component issues
    component_id=mycomponent.id,
    component_status=enums.COMPONENT_STATUS_MAJOR_OUTAGE,
)
```

.. and most other features supported by the Cachet API


## Local Development

Local setup:

```bash
python -m virtualenv .venv
. .venv/bin/activate
pip install -e .
```

## Tests

This project has a fairly extensive test setup.

* Unit tests are located in `tests/` including a fake
  implementation of the Cachet API.
* A simpler test script under `extras/live_run.py` that
  needs a running test instance of Cachet.

### Running unit tests

```bash
pip install -r tests/requirements.txt
tox

# Optionally
tox -e pep8  # for pep8 run only
tox -e py36  # tests only


# Running tests with pytest also works, but this works poorly in combination with environment variables for the live test script (tox separates environments)
pytest tests/
```

### Testing with real Cachet service

Do not run this script against a system in production.
This is only for a test service.
Cachet can easily be set up locally with docker: https://github.com/CachetHQ/Docker

Optionally we can run cachet from source: https://github.com/CachetHQ/Docker

A local setup is also located in the root or the repo (`docker-compose.yaml`).

You need to set the following environment variables.

```bash
CACHET_ENDPOINT
CACHET_API_TOKEN
```

Running tests:

```bash
python extras/live_run.py
...
=================================================
Number of tests   : 10
Successful        : 10
Failure           : 0
Percentage passed : 100.0%
=================================================
```

## Building Docs

```bash
pip install -r docs/requirements.txt
python setup.py build_sphinx
```

## Contributing

Do not hesitate opening issues or submit completed
or partial pull requests. Contributors of all
experience levels are welcome.

---
This project is sponsored by [zetta.io](https://www.zetta.io)

[![zetta.io](https://raw.githubusercontent.com/ZettaIO/cachet-client/master/.github/logo.png)](https://www.zetta.io)
