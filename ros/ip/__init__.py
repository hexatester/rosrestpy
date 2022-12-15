from attrs import define
from typing import List, Optional

from ros._base import BaseModule

from .address import Address
from .arp import ARP
from .cloud import Cloud
from .dhcp_client import DHCPClient
from .dhcp_relay import DHCPRelay
from .dhcp_server import DHCPServerModule
from .dns import DNS
from .route import Route
from .setting import Setting


@define
class IPModule(BaseModule):
    _dhcp_server: Optional[DHCPServerModule] = None

    def __attrs_post_init__(self) -> None:
        return super().__attrs_post_init__()

    def address(self, **kwds) -> List[Address]:
        return self.ros.get_as(self.url + "/address", List[Address], kwds)

    def arp(self, **kwds) -> List[ARP]:
        return self.ros.get_as(self.url + "/arp", List[ARP], kwds)

    @property
    def cloud(self) -> Cloud:
        return self.ros.get_as(self.url + "/cloud", Cloud)

    def dhcp_client(self, **kwds) -> List[DHCPClient]:
        return self.ros.get_as(self.url + "/dhcp-client", List[DHCPClient], kwds)

    def dhcp_relay(self, **kwds) -> List[DHCPRelay]:
        return self.ros.get_as(self.url + "/dhcp-relay", List[DHCPRelay], kwds)

    @property
    def dhcp_server(self) -> DHCPServerModule:
        if not self._dhcp_server:
            self._dhcp_server = DHCPServerModule(self, "/dhcp-server")
        return self._dhcp_server

    @property
    def dns(self) -> DNS:
        dns = self.ros.get_as(self.url + "/dns", DNS)
        dns._mod = self
        return dns

    def route(self, **kwds) -> List[Route]:
        return self.ros.get_as(self.url + "/route", List[Route], kwds)

    @property
    def setting(self) -> Setting:
        return self.ros.get_as(self.url + "/setting", Setting)


__all__ = [
    "Address",
    "ARP",
    "IPModule",
    "Cloud",
    "DHCPClient",
    "DHCPRelay",
    "DHCPServer",
    "DNS",
    "Route",
    "Setting",
]
