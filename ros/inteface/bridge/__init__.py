from attrs import define
from typing import Any, List

from ros._base import BaseProps

from .bridge import Bridge
from .msti import BridgeMsti
from .port import BridgePort
from .vlan import BridgeVlan


@define
class BridgeModule(BaseProps[Bridge]):
    @property
    def msti(self) -> List[BridgeMsti]:
        return self.ros.get_as(self.url + "/msti", List[BridgeMsti])

    @property
    def port(self) -> List[BridgePort]:
        return self.ros.get_as(self.url + "/port", List[BridgePort])

    @property
    def vlan(self) -> List[BridgeVlan]:
        return self.ros.get_as(self.url + "/vlan", List[BridgeVlan])


__all__ = ["BridgeModule", "BridgeInterface", "BridgePort", "Bridge"]
