from attr import define
from typing import Any, List

from ros._base import BaseSubModule

from .ethernet import InterfaceEthernet


@define
class EthernetModule(BaseSubModule):
    def __call__(self, **kwds: Any) -> List[InterfaceEthernet]:
        return self.print(**kwds)

    def print(self, **kwds) -> List[InterfaceEthernet]:
        return self.module.ros.get_as(self.url, List[InterfaceEthernet], kwds)


__all__ = ["InterfaceEthernet", "EthernetModule"]
