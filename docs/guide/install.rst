
Install
=======

A package is available on PyPI::

   pip install cachet-client

Bulding from source::

   git clone https://github.com/ZettaIO/cachet-client.git (or use ssh)
   python setup.py bdist_wheel
   # .whl will be located in dist/ directory and can be installed later with pip

Development Setup
-----------------

Development install::

   git clone https://github.com/ZettaIO/cachet-client.git (or use ssh)
   cd cachet-client
   python -m virtualenv .venv
   . .venv/bin/activate
   pip install -e .

Building docs::

   pip install -r docs/requirements.txt
   python setup.py build_sphinx

Running unit tests::

   pip install -r tests/requirements.txt
   tox

   # Optionally
   tox -e py36  # tests only
   tox -e pep8  # for pep8 run only

   # Running tests wity pytest also works, but this works poorly in combination
   # with enviroment variables for the live test script (tox separates enviroments)
   pytest tests/

Testing with real Cachet service
--------------------------------

Do not run this script againt a system in production.
This is only for a test service. Cachet can easily be set up locally
with docker: https://github.com/CachetHQ/Docker

You need to set the following environment variables::

   CACHET_ENDPOINT
   CACHET_API_TOKEN

Running tests::

   python extras/live_run.py
   ...
   =================================================
   Numer of tests    : 10
   Succesful         : 10
   Failure           : 0
   Percentage passed : 100.0%
   =================================================
