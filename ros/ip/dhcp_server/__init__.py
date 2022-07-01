from typing import List

from ros.base import BaseSubModule
from .item import DHCPServerItem


class DHCPServer(BaseSubModule):
    url: str = "dhcp-server"

    @property
    def print(self) -> List[DHCPServerItem]:
        return self.ros.get_as(self.url, List[DHCPServerItem])


__all__ = ["DHCPServer", "DHCPServerItem"]
