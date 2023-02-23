from typing import Optional

from ros._base import BaseModule, BaseProps

from .address import Address
from .arp import ARP
from .cloud import Cloud
from .dhcp_client import DHCPClient
from .dhcp_relay import DHCPRelay
from .dhcp_server import DHCPServerModule, DHCPServer
from .dns import DNS
from .firewall import IPFirewallModule
from .route import Route
from .setting import Setting


class IPModule(BaseModule):
    _dhcp_server: Optional[DHCPServerModule] = None
    _firewall: Optional[IPFirewallModule] = None

    _address: BaseProps[Address] = None
    _arp: BaseProps[ARP] = None
    _dhcp_client: BaseProps[DHCPClient] = None
    _dhcp_relay: BaseProps[DHCPRelay] = None
    _route: BaseProps[Route] = None

    def __attrs_post_init__(self) -> None:
        return super().__attrs_post_init__()

    @property
    def address(self):
        if not self._address:
            self._address = BaseProps(self, self.url + "/address", Address)
        return self._address

    @property
    def arp(self):
        if not self._arp:
            self._arp = BaseProps(self, self.url + "/arp", ARP)
        return self._arp

    @property
    def cloud(self) -> Cloud:
        return self.ros.get_as(self.url + "/cloud", Cloud)

    @property
    def dhcp_client(self):
        if not self._dhcp_client:
            self._dhcp_client = BaseProps(self, self.url + "/dhcp-client", DHCPClient)
        return self._dhcp_client

    @property
    def dhcp_relay(self):
        if not self._dhcp_relay:
            self._dhcp_relay = BaseProps(self, self.url + "/dhcp-relay", DHCPRelay)
        return self._dhcp_relay

    @property
    def dhcp_server(self) -> DHCPServerModule:
        if not self._dhcp_server:
            self._dhcp_server = DHCPServerModule(
                self, self.url + "/dhcp-server", DHCPServer
            )
        return self._dhcp_server

    @property
    def dns(self) -> DNS:
        dns = self.ros.get_as(self.url + "/dns", DNS)
        dns._mod = self
        return dns

    @property
    def firewall(self) -> IPFirewallModule:
        if not self._firewall:
            self._firewall = IPFirewallModule(self, self.url + "/firewall")
        return self._firewall

    @property
    def route(self):
        if not self._route:
            self._route = BaseProps(self, self.url + "/route", Route)
        return self._route

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
