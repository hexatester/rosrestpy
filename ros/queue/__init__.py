from attrs import define
from typing import List

from ros._base import BaseModule
from ros._utils import make_setters
from .interface import InterfaceQueue
from .simple import SimpleQueue


@define
class QueueModule(BaseModule):
    @property
    def interface(self) -> List[InterfaceQueue]:
        return self.ros.get_as(self.url + "/interface", List[InterfaceQueue])

    @property
    def simple(self) -> List[SimpleQueue]:
        return self.ros.get_as(self.url + "/simple", List[SimpleQueue])

    simple.setter(make_setters("/queue/simple", SimpleQueue))
