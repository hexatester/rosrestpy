from typing import List
from ros.base import BaseModule

from .item import InterfaceItem


class Interface(BaseModule):
    def print(self) -> List[InterfaceItem]:
        return self.ros.get_as(self.url, List[InterfaceItem])


__all__ = ["Interface", "InterfaceItem"]
