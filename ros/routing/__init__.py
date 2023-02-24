from ros._base import BaseModule, BaseProps

from .table import RoutingTable


class RoutingModule(BaseModule):
    _table: BaseProps[RoutingTable] = None

    @property
    def table(self):
        if not self._table:
            self._table = BaseProps(self.ros, "/routing/table", RoutingTable)
        return self._table


__all__ = ["RoutingModule", "RoutingTable"]
