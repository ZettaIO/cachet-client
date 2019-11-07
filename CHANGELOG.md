
# 2.0.1

* Fix Internal Server Error when creating incidents due to
  empty `vars`. (Likely a 2.4+ issue)

# 2.0.0

* Python 3.8 support
* Fix embarrasing class name typo `CompontentGroup` -> `ComponentGroup`
* Fix embarrasing class name typo `CompontentGroupManager` -> `ComponentGroupManager`
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
