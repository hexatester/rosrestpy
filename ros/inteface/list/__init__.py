from typing import List
from attr import define

from ros._base import BaseSubModule

from .list import InterfaceList
from .member import InterfaceListMember


@define
class InterfaceListModule(BaseSubModule):
    def print(self) -> List[InterfaceList]:
        return self.module.ros.get_as(self.url, List[InterfaceList])

    @property
    def member(self) -> List[InterfaceListMember]:
        return self.module.ros.get_as(self.url + "/member", List[InterfaceListMember])


__all__ = ["InterfaceList", "InterfaceListMember", "InterfaceListModule"]
