from attrs import define
from typing import List, Optional

from ros.base import BaseModule

from .address import Address
from .arp import ARP
from .cloud import Cloud
from .dhcp_client import DHCPClient
from .dhcp_relay import DHCPRelay
from .dhcp_server import DHCPServer
from .dns import DNS
from .route import Route
from .setting import Setting


@define
class IP(BaseModule):
    _dhcp_server: Optional[DHCPServer] = None

    def __attrs_post_init__(self) -> None:
        return super().__attrs_post_init__()

    @property
    def address(self) -> List[Address]:
        return self.ros.get_as(self.url + "/address", List[Address])

    @property
    def arp(self) -> List[ARP]:
        return self.ros.get_as(self.url + "/arp", List[ARP])

    @property
    def cloud(self) -> Cloud:
        return self.ros.get_as(self.url + "/cloud", Cloud)

    @property
    def dhcp_client(self) -> List[DHCPClient]:
        return self.ros.get_as(self.url + "/dhcp-client", List[DHCPClient])

    @property
    def dhcp_relay(self) -> List[DHCPRelay]:
        return self.ros.get_as(self.url + "/dhcp-relay", List[DHCPRelay])

    @property
    def dhcp_server(self) -> DHCPServer:
        if not self._dhcp_server:
            self._dhcp_server = DHCPServer(self, "dhcp-server")
        return self._dhcp_server

    @property
    def dns(self) -> DNS:
        return self.ros.get_as(self.url + "/dns", DNS)

    @property
    def route(self) -> List[Route]:
        return self.ros.get_as(self.url + "/route", List[Route])

    @property
    def setting(self) -> Setting:
        return self.ros.get_as(self.url + "/setting", Setting)


__all__ = [
    "Address",
    "ARP",
    "IP",
    "Cloud",
    "DHCPClient",
    "DHCPRelay",
    "DHCPServer",
    "DNS",
    "Route",
    "Setting",
]
