# Creating a release

- Bump version in `setup.py`, `__init__.py` and `docs/conf.py`
- run `tox` or ensure CI passed
- Ensure docs are updated
- `twine upload dist/...`
- Create release in github
- Ensure new docs are built on RTD
