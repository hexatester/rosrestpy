from typing import List

from ros._base import BaseModule

from .table import RoutingTable


class RoutingModule(BaseModule):
    @property
    def table(self) -> List[RoutingTable]:
        return self.ros.get_as(self.url + "/table", List[RoutingTable])


__all__ = ["RoutingModule", "RoutingTable"]
