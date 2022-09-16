from attrs import define

from ros._base import BaseModule
from .simple import SimpleQueue

@define
class QueueModule(BaseModule):
    @property
    def simple(self) -> SimpleQueue:
        return self.ros.get_as(self.url + "/simple", SimpleQueue)
