from attrs import define
from typing import Any, List

from ros._base import BaseModule
from ros._utils import make_setters
from .interface import InterfaceQueue
from .simple import SimpleQueue


@define
class QueueModule(BaseModule):
    def interface(self, **kwds: Any) -> List[InterfaceQueue]:
        return self.ros.get_as(self.url + "/interface", List[InterfaceQueue], kwds)

    def simple(self, **kwds: Any) -> List[SimpleQueue]:
        return self.ros.get_as(self.url + "/simple", List[SimpleQueue], kwds)
