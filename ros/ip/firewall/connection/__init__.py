from typing import Any, List

from ros._base import BaseSubModule
from .connection import IPConnection


class IPFirewallConnectionModule(BaseSubModule):
    def __call__(self, **kwds: Any) -> List[IPConnection]:
        return self.print(**kwds)

    def print(self, **kwds: Any) -> List[IPConnection]:
        return self.module.ros.get_as(self.url, List[IPConnection], kwds)
