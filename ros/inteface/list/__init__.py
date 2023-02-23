from attr import define
from typing import Optional, List

from ros._base import BaseProps

from .list import InterfaceList
from .member import InterfaceListMember


@define
class InterfaceListModule(BaseProps[InterfaceList]):
    _member: Optional[BaseProps[InterfaceListMember]] = None

    @property
    def member(self) -> BaseProps[InterfaceListMember]:
        if not self._member:
            self._member = BaseProps(self.mod, "/list/member", InterfaceListMember)
        return self._member


__all__ = ["InterfaceList", "InterfaceListMember", "InterfaceListModule"]
