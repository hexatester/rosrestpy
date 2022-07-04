from typing import List

from ros._base import BaseModule

from .ping import Ping


class ToolModule(BaseModule):
    def ping(self, address: str, count: int = 4):
        data = {"address": address, "count": count}
        return self.ros.post_as("/ping", List[Ping], data)
