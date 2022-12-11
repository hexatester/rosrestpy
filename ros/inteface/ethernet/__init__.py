from typing import List
from attr import define

from ros._base import BaseSubModule

from .ethernet import InterfaceEthernet


@define
class EthernetModule(BaseSubModule):
    def print(self) -> List[InterfaceEthernet]:
        return self.module.ros.get_as(self.url, List[InterfaceEthernet])


__all__ = ["InterfaceEthernet", "EthernetModule"]
