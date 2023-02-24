from typing import Any, List

from ros._base import BaseModule, BaseProps

from .bridge import BridgeModule, Bridge, BridgeMsti, BridgePort, BridgeVlan
from .ethernet import InterfaceEthernet
from .interface import Interface
from .list import InterfaceList, InterfaceListMember, InterfaceListModule


class InterfaceModule(BaseModule):
    _brigde: BridgeModule = None
    _ethernet: BaseProps[InterfaceEthernet] = None
    _list: InterfaceListModule = None

    def __call__(self, **kwds: Any):
        return self.print(**kwds)

    @property
    def bridge(self) -> BridgeModule:
        if not self._brigde:
            self._brigde = BridgeModule(self.ros, "/interface/bridge", Bridge)
        return self._brigde

    @property
    def list(self) -> InterfaceListModule:
        if not self._list:
            self._list = InterfaceListModule(self.ros, "/interface/list", InterfaceList)
        return self._list

    @property
    def ethernet(self) -> BaseProps[InterfaceEthernet]:
        if not self._ethernet:
            self._ethernet = BaseProps(
                self.ros, "/interface/ethernet", InterfaceEthernet
            )
            self._ethernet._create = False
            self._ethernet._delete = False
        return self._ethernet

    def print(self, **kwds: Any) -> List[Interface]:
        return self.ros.get_as(self.url, List[Interface], kwds)


__all__ = [
    "BridgeModule",
    "Bridge",
    "BridgeMsti",
    "BridgePort",
    "BridgeVlan",
    "EthernetModule",
    "InterfaceModule",
    "Interface",
    "InterfaceList",
    "InterfaceListMember",
    "InterfaceListModule",
]
