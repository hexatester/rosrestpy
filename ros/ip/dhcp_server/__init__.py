from typing import List

from ros._base import BaseProps
from .dhcp_server import DHCPServer
from .lease import DHCPLease
from .network import DHCPNetwork


class DHCPServerModule(BaseProps[DHCPServer]):
    _lease: BaseProps[DHCPLease] = None

    @property
    def lease(self) -> BaseProps[DHCPLease]:
        if not self._lease:
            self._lease = BaseProps(self.ros, "/ip/dhcp-server/lease", DHCPLease)
        return self._lease

    @property
    def network(self) -> List[DHCPNetwork]:
        return self.ros.get_as(self.filename + "/network", List[DHCPNetwork])


__all__ = ["DHCPNetwork", "DHCPServerModule", "DHCPServer", "DHCPLease"]
