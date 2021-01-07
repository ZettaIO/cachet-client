from datetime import datetime
from typing import Generator, Optional

from cachetclient.base import Manager, Resource
from cachetclient import utils


class MetricPoint(Resource):
    @property
    def id(self) -> int:
        """int: unique id of the metric point"""
        return self.get("id")

    @property
    def metric_id(self) -> int:
        """int: Get or set metic id for this metric point"""
        return self.get("metric_id")

    @metric_id.setter
    def metric_id(self, value: int):
        self._data["metric_id"] = value

    @property
    def value(self) -> float:
        """float: Value to plot on the metric graph"""
        return self.get("value")

    @value.setter
    def value(self, value: float):
        self._data["value"] = value

    @property
    def created_at(self) -> Optional[datetime]:
        """datetime: When the metric point was created"""
        return utils.to_datetime(self.get("created_at"))

    @property
    def updated_at(self) -> Optional[datetime]:
        """datetime: Last time the issue was updated"""
        return utils.to_datetime(self.get("updated_at"))

    @property
    def counter(self) -> int:
        """int: Show the actual calculated value"""
        return self.get("counter")

    @counter.setter
    def counter(self, value: float):
        self._data["counter"] = value

    @property
    def calculated_value(self) -> float:
        """float: The calculated value on metric graph"""
        return self.get("calculated_value")

    @calculated_value.setter
    def calculated_value(self, value: float):
        self._data["calculated_value"] = value


class MetricPointsManager(Manager):
    resource_class = MetricPoint
    path = "metrics/{}/points"

    def create(self, *, metric_id: int, value: float) -> MetricPoint:
        """
        Create an metric point

        Keyword Args:
            metric_id (int): The metric to tag with the point
            value (fload): Metric point value for graph

        Returns:
            :py:data:`MetricPoint` instance
        """
        return self._create(self.path.format(metric_id), {"value": value})

    def count(self, metric_id) -> int:
        """
        Count the number of metric points for a metric

        Args:
            metric_id (int): The metric

        Returns:
            int: Number of metric points for the metric
        """
        return self._count(self.path.format(metric_id))

    def list(
        self, metric_id: int, page: int = 1, per_page: int = 20
    ) -> Generator[MetricPoint, None, None]:
        """
        List updates for a metric

        Args:
            metric_id: The metric id to list updates

        Keyword Args:
            page (int): The first page to request
            per_page (int): Entries per page

        Return:
            Generator of :py:data:`MetricPoint`
        """
        yield from self._list_paginated(
            self.path.format(metric_id), page=page, per_page=per_page
        )

    def delete(self, metric_id: int, point_id: int) -> None:
        """
        Delete a metric point
        """
        self._delete(self.path.format(metric_id), point_id)
