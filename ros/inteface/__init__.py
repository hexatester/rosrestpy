from typing import List
from ros._base import BaseModule

from .interface import Interface


class InterfaceModule(BaseModule):
    def print(self) -> List[Interface]:
        return self.ros.get_as(self.url, List[Interface])


__all__ = ["InterfaceModule", "Interface"]
