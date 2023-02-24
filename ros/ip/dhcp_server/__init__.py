from typing import List

from ros._base import BaseProps
from .dhcp_server import DHCPServer
from .lease import DHCPLease
from .network import DHCPNetwork


class DHCPServerModule(BaseProps[DHCPServer]):
    _lease: BaseProps[DHCPLease] = None
    _network: BaseProps[DHCPNetwork] = None

    @property
    def lease(self) -> BaseProps[DHCPLease]:
        if not self._lease:
            self._lease = BaseProps(self.ros, "/ip/dhcp-server/lease", DHCPLease)
        return self._lease

    @property
    def network(self) -> BaseProps[DHCPNetwork]:
        if not self._network:
            self._network = BaseProps(self.ros, "/ip/dhcp-server/network", DHCPNetwork)
        return self._network


__all__ = ["DHCPNetwork", "DHCPServerModule", "DHCPServer", "DHCPLease"]
