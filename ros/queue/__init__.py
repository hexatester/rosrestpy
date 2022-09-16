from attrs import define
from typing import List

from ros._base import BaseModule
from .simple import SimpleQueue

@define
class QueueModule(BaseModule):
    @property
    def simple(self) -> List[SimpleQueue]:
        return self.ros.get_as(self.url + "/simple", List[SimpleQueue])
