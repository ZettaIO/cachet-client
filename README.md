[![pypi](https://badge.fury.io/py/cachet-client.svg)](https://pypi.python.org/pypi/cachet-client)
[![travis](https://api.travis-ci.org/ZettaIO/cachet-client.svg?branch=master)](https://travis-ci.org/ZettaIO/cachet-client)

# cachet-client

A python 3 API client for then open source status page system
[Cachet](https://github.com/CachetHQ/Cachet).

* [cachet-client on github](https://github.com/ZettaIO/cachet-client)
* [cachet-client on PyPI](https://pypi.org/project/cachet-client/)
* Documentation (WIP)

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
* Hopefully good documentation (soon!?)

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

# Check if api is responding
if client.ping():
    print("Cachet is up and running!")

# Create and delete a subscriber
sub = client.subscribers.create('user@example.test', verify=True)
sub.delete()

# List all subscribers paginated (generator)
for sub in client.subscribers.list():
    print(sub.id, sub.email)

# Create an issue
issue = client.incidents.create(
    "Something blew up!",
    "We are looking into it",
    enums.INCIDENT_INVESTIGATING,
    component_status=enums.COMPONENT_STATUS_MAJOR_OUTAGE,
)

# .. and most other features supported by the Cachet API
```


## Local Development

Local setup:

```bash
python3.7 -m virtualenv .venv
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
tox -e py36  # tests only
tox -e pep8  # for pep8 run only

# Running tests wity pytest also works, but this works poorly in combination with enviroment variables for the live test script (tox separates enviroments)
pytest tests/
```

### Testing with real Cachet service

Do not run this script againt a system in production.
This is only for a test service.
Cachet can easily be set up locally with docker: https://github.com/CachetHQ/Docker


You need to set the following environment variables.

```bash
CACHET_ENDPOINT
CACHET_API_TOKEN
```

Running tests:

```bash
python3.7 extras/live_run.sh
...
=================================================
Numer of tests    : 10
Succesful         : 8
Failure           : 2
Percentage passed : 80.0%
=================================================
```

## Contributing

Do not hesitete opening issues or submit completed
or partial pull requests. Contributors of all
experience levels are welcome.
