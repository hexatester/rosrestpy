from typing import List
from attr import define

from ros._base import BaseSubModule

from .ethernet import EthernetList


@define
class EthernetModule(BaseSubModule):
    def print(self) -> List[EthernetList]:
        return self.module.ros.get_as(self.url, List[EthernetList])


__all__ = ["EthernetList", "EthernetModule"]
