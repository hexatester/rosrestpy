from typing import List

from ros.base import BaseSubModule
from .item import DHCPServerItem
from .network import DHCPNetwork


class DHCPServer(BaseSubModule):
    url: str = "dhcp-server"

    def print(self) -> List[DHCPServerItem]:
        return self.module.ros.get_as(self.url, List[DHCPServerItem])

    @property
    def network(self) -> List[DHCPNetwork]:
        return self.module.ros.get_as(self.url + "/network", List[DHCPNetwork])


__all__ = ["DHCPNetwork", "DHCPServer", "DHCPServerItem"]
