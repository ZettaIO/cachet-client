
# 4.0.1

Drop python 3.5 support.

# 4.0.0

## Tags

Revamped how we interact with component tags. Previous
versions was limited to inspecting component slugs.

* ``Component.tags`` now returns a slug:name dict
* ``Component.tag_names`` returns a list of tag names
* ``Component.tag_slugs`` returns a list of slug names
* ``Components.tags`` are now read-only
* ``Components.set_tags()`` will overwrite all tags
* ``Components.add_tag`` and ``add_tags`` can be used to add tags
* All tag lookups are now case insensitive

## Other Additions / Fixes

* Incidents now support the ``occurred_at`` field in cachet 2.4
* Updating components via incidents should no longer cause a 400 error if
  `component_id` or `component_status` is missing

# 3.1.1

* Added missing resource imports in `v1.__init__`
* Removed irrelevant `__version__` value in `cachetclient.v1.__init__`

# 3.1.0

* Added support for schedules (cachet 2.4)

# 3.0.0

## Additions / Improvements

* Support for metrics and metric points
* Documentation improvements

## Breaking changes

* Fixed class name typo: `IncidentUpdate` properly renamed to `IncidentUpdate`
* `IncidentUpdate.permlink` renamed to `permalink` (in line with the actual field name)

# 2.0.1

* Fix Internal Server Error when creating incidents due to
  empty `vars`. (Likely a 2.4+ issue)

# 2.0.0

* Python 3.8 support
* Fix class name typo `CompontentGroup` -> `ComponentGroup`
* Fix class name typo `CompontentGroupManager` -> `ComponentGroupManager`
* Various other typos
* ComponentGroup now supports the `visible` flag

# 1.3.0

* All managers now support `instance_list_from_json`
  to greatly ease re-creation of resource objects lists
  stored in databases or caches as json.

# 1.2.0

* All resource instances can now be re-created using `instance_from_dict` and `instance_from_json`.
* Some doc improvements

# 1.1.0

* Downgraded python requirement to 3.5. Currently there are no reasons to require 3.6+
* `ComponentGroup` now has the `enabled_components` property.
* Tests are now run in py3.5, py3.6 and py3.7 environments using `tox`.

# 1.0.0

* First stable version
* Some method signatures have changed
* Richer docstrings + Docs.

# 0.9.0

Initial release. We will move towards 1.0 until we are 2.4 complete.
