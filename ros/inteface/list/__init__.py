from attr import define
from typing import Any, List

from ros._base import BaseSubModule

from .list import InterfaceList
from .member import InterfaceListMember


@define
class InterfaceListModule(BaseSubModule):
    def __call__(self, **kwds: Any) -> Any:
        return self.print(**kwds)

    def print(self, **kwds) -> List[InterfaceList]:
        return self.module.ros.get_as(self.url, List[InterfaceList], kwds)

    @property
    def member(self) -> List[InterfaceListMember]:
        return self.module.ros.get_as(self.url + "/member", List[InterfaceListMember])


__all__ = ["InterfaceList", "InterfaceListMember", "InterfaceListModule"]
