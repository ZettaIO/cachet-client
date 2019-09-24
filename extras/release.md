# Creating a release

- Bump version in `setup.py` and `__init__.py`
- run `tox`
- Ensure docs are updated
- `twine upload dist/...`
- Create release in github
- Ensure new docs are built on RTD
