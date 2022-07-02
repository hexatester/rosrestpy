from typing import List
from attrs import define

from ros._base import BaseModule

from .bridge import Bridge


@define
class BridgeModule(BaseModule):
    def print(self) -> List[Bridge]:
        return self.ros.get_as(self.url, List[Bridge])


__all__ = ["BridgeModule", "BridgeInterface"]
