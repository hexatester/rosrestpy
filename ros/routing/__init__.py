from typing import Any, List

from ros._base import BaseModule

from .table import RoutingTable


class RoutingModule(BaseModule):
    def table(self, **kwds: Any) -> List[RoutingTable]:
        return self.ros.get_as(self.url + "/table", List[RoutingTable], kwds)


__all__ = ["RoutingModule", "RoutingTable"]
