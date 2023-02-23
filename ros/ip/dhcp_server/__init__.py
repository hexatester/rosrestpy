from typing import List

from ros._base import BaseProps
from .dhcp_server import DHCPServer
from .network import DHCPNetwork


class DHCPServerModule(BaseProps[DHCPServer]):
    @property
    def network(self) -> List[DHCPNetwork]:
        return self.ros.get_as(self.filename + "/network", List[DHCPNetwork])


__all__ = ["DHCPNetwork", "DHCPServerModule", "DHCPServer"]
