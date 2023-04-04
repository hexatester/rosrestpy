from ros._base import BaseModule, BaseProps

from .rule import RoutingRule
from .table import RoutingTable


class RoutingModule(BaseModule):
    _rule: BaseProps[RoutingRule] = None
    _table: BaseProps[RoutingTable] = None

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


__all__ = ["RoutingModule", "RoutingTable"]
