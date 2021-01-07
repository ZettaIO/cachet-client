import json
from typing import Any, Generator, Optional, List

from cachetclient.httpclient import HttpClient


class Resource:
    """Bag of attributes"""

    def __init__(self, manager, data):
        """Resource initializer.

        Args:
            manager: The manager this resource belongs to
            data: The raw json data
        """
        self._manager = manager
        self._data = data

    @property
    def attrs(self) -> dict:
        """dict: The raw json response from the server"""
        return self._data

    def get(self, name) -> Any:
        """
        Safely obtain any attribute name for the resource

        Args:
            name (str): Key name in json response

        Returns:
            Value from the raw json response.
            If the key doesn't exist ``None`` is returned.
        """
        return self._data.get(name)

    def update(self):
        """
        Posts the values in the resource to the server.

        Example::

            # Change an attribute and save the resource
            >> resource.value = something
            >> updated_resource = resource.update()

        Returns:
            Resource: The updated resource from the server
        """
        return self._manager.update(self.get("id"), **self.attrs)

    def delete(self) -> None:
        """
        Deletes the resource from the server.
        
        Raises:
            HTTPException if the resource don't exist.
        """
        self._manager.delete(self.get("id"))

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return str(self._data)


class Manager:
    """
    Base class for handling crud resources
    """

    resource_class = Resource
    path: Optional[str] = None

    def __init__(self, http_client: HttpClient):
        """Manager initializer.

        Args:
            http_client: The httpclient
        """
        self._http = http_client

        if self.resource_class is None:
            raise ValueError(
                "resource_class not defined in class {}".format(self.__class__)
            )

        # if self.path is None:
        #     raise ValueError("path not defined for class {}".format(self.__class__))

    def instance_from_dict(self, data: dict) -> Resource:
        """Creates a resource instance from a dictionary.

        This doesn't hit any endpoints in cachet, but rather
        enables us to create a resource class instance from
        dictionary data. This can be useful when caching
        data from cachet in memcache or databases.

        Args:
            data (dict): dictionary containing the instance data
        Returns:
            Resource: The resource class instance
        """
        return self.resource_class(self, data)

    def instance_from_json(self, data: str) -> Resource:
        """Creates a resource instance from a json string.

        This doesn't hit any endpoints in cachet, but rather
        enables us to create a resource class instance from
        json data. This can be useful when caching
        data from cachet in memcache or databases.

        Args:
            data (str): json string containing the instance data
        Returns:
            Resource: The resource class instance
        """
        return self.resource_class(self, json.loads(data))

    def instance_list_from_json(self, data: str) -> List[Resource]:
        """Creates a resource instance list from a json string.

        This doesn't hit any endpoints in cachet, but rather
        enables us to create a resource class instances from
        json data. This can be useful when caching
        data from cachet in memcache or databases.

        Args:
            data (str): json string containing the instance data
        Returns:
            Resource: The resource class instance
        Raises:
            ValueError: if json data do not deserialize into a list
        """
        instances = json.loads(data)
        if not isinstance(instances, list):
            raise ValueError(
                "json data is {}, not a list : {}".format(type(instances), instances)
            )

        return [self.resource_class(self, inst) for inst in instances]

    def _create(self, path: str, data: dict):
        response = self._http.post(path, data=data)
        return self.resource_class(self, response.json()["data"])

    def _update(self, path: str, resource_id: int, data: dict) -> Resource:
        """Generic resource updater

        Args:
            path (str): url path relative to base url
            resource_id (int): The resource to update
            data (dict): New data

        Returns:
            Resource: The updated resource from the server
        """
        response = self._http.put("{}/{}".format(path, resource_id), data=data)
        return self.resource_class(self, response.json()["data"])

    def _list_paginated(
        self, path: str, page=1, per_page=20
    ) -> Generator[Resource, None, None]:
        """List resources paginated.

        Args:
            path (str): url path relative to base url

        Keyword Args:
            page (int): Page to start on
            per_page (int): Number of entries per page

        Returns:
            Generator of resources
        """
        while True:
            result = self._http.get(
                path,
                params={
                    "page": page,
                    "per_page": per_page,
                },
            )
            json_data = result.json()

            meta = json_data["meta"]
            data = json_data["data"]

            for entry in data:
                yield self.resource_class(self, entry)

            if page >= meta["pagination"]["total_pages"]:
                break

            page += 1

    # def _search(self, path, params=None):
    #     params = params or {}
    #     result = self._http.get(path, params={'per_page': 1, **params})
    #     json_data = result.json()

    def _get(self, path: str, resource_id: int):
        """Generic resource getter (single)

        Args:
            path (str): url path relative to base url
            resource_id (int): The resource id to get

        Returns:
            :py:data:`Resource`: A resource instance
        """
        result = self._http.get("{}/{}".format(path, resource_id))
        json_data = result.json()
        return self.resource_class(self, json_data["data"])

    def _count(self, path: str) -> int:
        """Generic count method
        using the pagination system to obtain the total number of resources

        Args:
            path (str): url path relative to base url

        Returns:
            int: Number of resources
        """
        result = self._http.get(path, params={"per_page": 1})
        json_data = result.json()
        return json_data["meta"]["pagination"]["total"]

    def _delete(self, path: str, resource_id: int) -> None:
        """Generic resource deleter

        Args:
            path (str): url path relative to base url
            resource_id (int): The resource to delete
        """
        self._http.delete(path, resource_id)

    def _build_data_dict(self, **kwargs) -> dict:
        """Builds a data dictionary for posting to the server.

        Will omit key/value pars with None values.
        This makes partial updates less error prone.

        Returns:
            dict: dict without `None` values
        """
        return {key: value for key, value in kwargs.items() if value is not None}
