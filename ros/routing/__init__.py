from ros._base import BaseModule, BaseProps

from .id import RoutingId
from .nexthop import Nexthop
from .rule import RoutingRule
from .table import RoutingTable


class RoutingModule(BaseModule):
    _id: BaseProps[RoutingId] = None
    _nexthop: BaseProps[Nexthop] = None
    _rule: BaseProps[RoutingRule] = None
    _table: BaseProps[RoutingTable] = None

    @property
    def id(self):
        if not self._id:
            self._id = BaseProps(self.ros, "/routing/id", RoutingId)
        return self._id

    @property
    def nexthop(self):
        if not self._nexthop:
            self._nexthop = BaseProps(self.ros, "/routing/nexthop", Nexthop)
        return self._nexthop

    @property
    def rule(self):
        if not self._rule:
            self._rule = BaseProps(self.ros, "/routing/rule", RoutingRule)
        return self._rule

    @property
    def table(self):
        if not self._table:
            self._table = BaseProps(self.ros, "/routing/table", RoutingTable)
        return self._table


__all__ = ["RoutingId", "Nexthop", "RoutingModule", "RoutingTable"]
