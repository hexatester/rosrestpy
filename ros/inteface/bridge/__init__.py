from typing import List
from attrs import define

from ros._base import BaseSubModule

from .bridge import Bridge
from .port import BridgePort


@define
class BridgeModule(BaseSubModule):
    def print(self) -> List[Bridge]:
        return self.module.ros.get_as(self.url, List[Bridge])

    @property
    def port(self) -> List[BridgePort]:
        return self.module.ros.get_as(self.url + "/port", List[BridgePort])


__all__ = ["BridgeModule", "BridgeInterface", "BridgePort"]
