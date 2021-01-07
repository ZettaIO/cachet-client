from datetime import datetime
from typing import Generator, Optional

from cachetclient.base import Manager, Resource
from cachetclient import utils
from cachetclient.v1.metric_points import MetricPointsManager
from cachetclient.httpclient import HttpClient


class Metric(Resource):
    @property
    def id(self) -> int:
        return self.get("id")

    @property
    def name(self) -> str:
        return self.get("name")

    @name.setter
    def name(self, value: str):
        self._data["name"] = value

    @property
    def suffix(self) -> str:
        return self.get("suffix")

    @suffix.setter
    def suffix(self, value: str):
        self._data["suffix"] = value

    @property
    def description(self):
        return self.get("description")

    @description.setter
    def description(self, value: str):
        self._data["description"] = value

    @property
    def calc_type(self):
        return self.get("calc_type")

    @calc_type.setter
    def calc_type(self, value: int):
        self._data["calc_type"] = value

    @property
    def default_value(self):
        return self.get("default_value")

    @default_value.setter
    def default_value(self, value: int):
        self._data["default_value"] = value

    @property
    def display_chart(self) -> int:
        return self.get("display_chart")

    @display_chart.setter
    def display_chart(self, value: int):
        self._data["display_chart"] = value

    @property
    def created_at(self) -> Optional[datetime]:
        """datetime: When the issue was created"""
        return utils.to_datetime(self.get("created_at"))

    @property
    def updated_at(self) -> Optional[datetime]:
        """datetime: Last time the issue was updated"""
        return utils.to_datetime(self.get("updated_at"))

    @property
    def places(self) -> int:
        return self.get("places")

    @places.setter
    def places(self, value: int):
        self._data["places"] = value

    @property
    def default_view(self) -> int:
        return self.get("default_view")

    @default_view.setter
    def default_view(self, value: int):
        self._data["default_view"] = value

    @property
    def threshold(self) -> int:
        return self.get("threshold")

    @threshold.setter
    def threshold(self, value: int):
        self._data["threshold"] = value

    @property
    def order(self) -> int:
        return self.get("order")

    @order.setter
    def order(self, value: int):
        self._data["order"] = value

    @property
    def visible(self) -> int:
        return self.get("visible")

    @visible.setter
    def visible(self, value: int):
        self._data["visible"] = value

    def points(self) -> Generator["Metric", None, None]:
        """Generator['Metric', None, None]: Metric points for this metric"""
        return self._manager.points.list(self.id)


class MetricsManager(Manager):
    resource_class = Metric
    path = "metrics"

    def __init__(
        self, http_client: HttpClient, metric_update_manager: MetricPointsManager
    ):
        super().__init__(http_client)
        self.points = metric_update_manager

    def create(
        self,
        *,
        name: str,
        description: str,
        suffix: str,
        default_value: int = 0,
        display_chart: int = 0
    ) -> Metric:
        """
        Create a metric.

        Keyword Args:
            name (str): Name/title of the metric
            description (str): Description of what the metric is measuring
            suffix (str): Measurments in
            default_value (int): The default value to use when a point is added
            display_chart (int): Whether to display the chart on the status page

        Returns:
            :py:data:`Metric` instance
        """
        return self._create(
            self.path,
            {
                "name": name,
                "description": description,
                "suffix": suffix,
                "default_value": default_value,
                "display_chart": display_chart,
            },
        )

    def list(self, page: int = 1, per_page: int = 1) -> Generator[Metric, None, None]:
        """
        List all metrics paginated

        Keyword Args:
            page (int): Page to start on
            per_page (int): entries per page

        Returns:
            Generator of :py:data:`Metric`s
        """
        return self._list_paginated(
            self.path,
            page=page,
            per_page=per_page,
        )

    def count(self) -> int:
        """
        Count the number of metrics

        Returns:
            int: Total number of metrics
        """
        return self._count(self.path)

    def get(self, metric_id: int) -> Metric:
        """
        Get a signle metric

        Args:
            metric_id (int): The metric id to get

        Returns:
            :py:data:`Metric` instance

        Raises:
            :py:data:`requests.exception.HttpError`: if metric do not exist
        """
        return self._get(self.path, metric_id)

    def delete(self, metric_id: int) -> None:
        """
        Delete an metric

        Args:
            metric_id (int): The metric id
        """
        self._delete(self.path, metric_id)
