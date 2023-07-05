from typing import Any, List

from ros._base import BaseModule, BaseProps

from .bridge import BridgeModule, Bridge, BridgeMsti, BridgePort, BridgeVlan
from .eoip import EoIP
from .ethernet import InterfaceEthernet
from .interface import Interface
from .list import InterfaceList, InterfaceListMember, InterfaceListModule
from .veth import Veth
from .vlan import Vlan
from .wireguard import WireguardModule, Wireguard
from .vrrp import Vrrp


class InterfaceModule(BaseModule):
    _brigde: BridgeModule = None
    _eoip: BaseProps[EoIP] = None
    _ethernet: BaseProps[InterfaceEthernet] = None
    _list: InterfaceListModule = None
    _veth: BaseProps[Veth] = None
    _vlan: BaseProps[Vlan] = None
    _vrrp: BaseProps[Vrrp] = None
    _wireguard: WireguardModule = None

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
    def eoip(self) -> BaseProps[EoIP]:
        if not self._eoip:
            self._eoip = BaseProps(self.ros, "/interface/eoip", EoIP)
        return self._eoip

    @property
    def ethernet(self) -> BaseProps[InterfaceEthernet]:
        if not self._ethernet:
            self._ethernet = BaseProps(
                self.ros, "/interface/ethernet", InterfaceEthernet
            )
            self._ethernet._create = False
            self._ethernet._delete = False
        return self._ethernet

    @property
    def veth(self) -> BaseProps[Veth]:
        if not self._veth:
            self._veth = BaseProps(self.ros, "/interface/veth", Veth)
        return self._veth

    @property
    def vlan(self) -> BaseProps[Vlan]:
        if not self._vlan:
            self._vlan = BaseProps(self.ros, "/interface/vlan", Vlan)
        return self._vlan

    @property
    def vrrp(self) -> BaseProps[Vrrp]:
        if not self._vrrp:
            self._vrrp = BaseProps(self.ros, "/interface/vrrp", Vrrp)
        return self._vrrp

    @property
    def wireguard(self) -> WireguardModule:
        if not self._wireguard:
            self._wireguard = WireguardModule(
                self.ros, "/interface/wireguard", Wireguard
            )
        return self._wireguard

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
