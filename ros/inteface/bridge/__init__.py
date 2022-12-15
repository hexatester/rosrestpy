from attrs import define
from typing import Any, List

from ros._base import BaseSubModule

from .bridge import Bridge
from .msti import BridgeMsti
from .port import BridgePort
from .vlan import BridgeVlan


@define
class BridgeModule(BaseSubModule):
    def __call__(self, **kwds: Any) -> List[Bridge]:
        return self.print(**kwds)

    def print(self, **kwds: Any) -> List[Bridge]:
        return self.module.ros.get_as(self.url, List[Bridge], kwds)

    @property
    def msti(self) -> List[BridgeMsti]:
        return self.module.ros.get_as(self.url + "/msti", List[BridgeMsti])

    @property
    def port(self) -> List[BridgePort]:
        return self.module.ros.get_as(self.url + "/port", List[BridgePort])

    @property
    def vlan(self) -> List[BridgeVlan]:
        return self.module.ros.get_as(self.url + "/vlan", List[BridgeVlan])


__all__ = ["BridgeModule", "BridgeInterface", "BridgePort"]
