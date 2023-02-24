from attrs import define

from ros._base import BaseProps

from .bridge import Bridge
from .msti import BridgeMsti
from .port import BridgePort
from .vlan import BridgeVlan


@define
class BridgeModule(BaseProps[Bridge]):
    _msti: BaseProps[BridgeMsti] = None
    _port: BaseProps[BridgePort] = None
    _vlan: BaseProps[BridgeVlan] = None

    @property
    def msti(self) -> BaseProps[BridgeMsti]:
        if not self._msti:
            self._msti = BaseProps(self.ros, "/interface/bridge/msti", BridgeMsti)
        return self._msti

    @property
    def port(self) -> BaseProps[BridgePort]:
        if not self._port:
            self._port = BaseProps(self.ros, "/interface/bridge/port", BridgePort)
        return self._port

    @property
    def vlan(self) -> BaseProps[BridgeVlan]:
        if not self._vlan:
            self._vlan = BaseProps(self.ros, "/interface/bridge/vlan", BridgeVlan)
        return self._vlan


__all__ = ["BridgeModule", "BridgeInterface", "BridgePort", "Bridge"]
