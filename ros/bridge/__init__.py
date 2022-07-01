from typing import List
from attrs import define

from ros.base import BaseModule

from .interface import BridgeInterface


@define
class Bridge(BaseModule):
    def print(self) -> List[BridgeInterface]:
        return self.ros.get_as(self.url, List[BridgeInterface])


__all__ = ["Bridge", "BridgeInterface"]
