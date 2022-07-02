from typing import List

from ros._base import BaseSubModule
from .dhcp_server import DHCPServer
from .network import DHCPNetwork


class DHCPServerModule(BaseSubModule):
    url: str = "dhcp-server"

    def print(self) -> List[DHCPServer]:
        return self.module.ros.get_as(self.url, List[DHCPServer])

    @property
    def network(self) -> List[DHCPNetwork]:
        return self.module.ros.get_as(self.url + "/network", List[DHCPNetwork])


__all__ = ["DHCPNetwork", "DHCPServerModule", "DHCPServer"]
