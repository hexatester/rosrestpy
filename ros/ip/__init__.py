from ros._base import BaseModule, BaseProps

from .address import Address
from .arp import ARP
from .cloud import Cloud
from .dhcp_client import DHCPClient
from .dhcp_relay import DHCPRelay
from .dhcp_server import DHCPServerModule, DHCPServer
from .dns import DNS
from .firewall import IPFirewallModule
from .hotspot import HotspotModule, HotspotServer
from .kid_control import KidControlModule, KidControl
from .neighbor import IPNeighbor
from .pool import IPPool
from .route import Route
from .service import Service
from .setting import Setting
from .vrf import Vrf


class IPModule(BaseModule):
    _dhcp_server: DHCPServerModule = None
    _firewall: IPFirewallModule = None
    _hotspot: HotspotModule = None

    _address: BaseProps[Address] = None
    _arp: BaseProps[ARP] = None
    _dhcp_client: BaseProps[DHCPClient] = None
    _dhcp_relay: BaseProps[DHCPRelay] = None
    _kid_control: KidControlModule = None
    _pool: BaseProps[IPPool] = None
    _neighbor: BaseProps[IPNeighbor] = None
    _route: BaseProps[Route] = None
    _service: BaseProps[Service] = None
    _vrf: BaseProps[Vrf] = None

    @property
    def address(self):
        if not self._address:
            self._address = BaseProps(self.ros, "/ip/address", Address)
        return self._address

    @property
    def arp(self):
        if not self._arp:
            self._arp = BaseProps(self.ros, "/ip/arp", ARP)
        return self._arp

    @property
    def cloud(self) -> Cloud:
        return self.ros.get_as("/ip/cloud", Cloud)

    @property
    def dhcp_client(self):
        if not self._dhcp_client:
            self._dhcp_client = BaseProps(self.ros, "/ip/dhcp-client", DHCPClient)
        return self._dhcp_client

    @property
    def dhcp_relay(self):
        if not self._dhcp_relay:
            self._dhcp_relay = BaseProps(self.ros, "/ip/dhcp-relay", DHCPRelay)
        return self._dhcp_relay

    @property
    def dhcp_server(self) -> DHCPServerModule:
        if not self._dhcp_server:
            self._dhcp_server = DHCPServerModule(
                self.ros, "/ip/dhcp-server", DHCPServer
            )
        return self._dhcp_server

    @property
    def dns(self) -> DNS:
        dns = self.ros.get_as("/ip/dns", DNS)
        dns._ros = self.ros
        return dns

    @property
    def firewall(self) -> IPFirewallModule:
        if not self._firewall:
            self._firewall = IPFirewallModule(self.ros, "/ip/firewall")
        return self._firewall

    @property
    def hotspot(self) -> HotspotModule:
        if not self._hotspot:
            self._hotspot = HotspotModule(self.ros, "/ip/hotspot", HotspotServer)
        return self._hotspot

    @property
    def kid_control(self) -> KidControlModule:
        if not self._kid_control:
            self._kid_control = KidControlModule(
                self.ros, "/ip/kid-control", KidControl
            )
        return self._kid_control

    @property
    def neighbor(self) -> BaseProps[IPNeighbor]:
        if not self._neighbor:
            self._neighbor = BaseProps(self.ros, "/ip/neighbor", IPNeighbor)
            self._neighbor._delete = False
            self._neighbor._write = False
            self._neighbor._disable = False
        return self._neighbor

    @property
    def pool(self) -> BaseProps[IPPool]:
        if not self._pool:
            self._pool = BaseProps(self.ros, "/ip/pool", IPPool)
            self._pool._disable = False
        return self._pool

    @property
    def route(self) -> BaseProps[Route]:
        if not self._route:
            self._route = BaseProps(self.ros, "/ip/route", Route)
        return self._route

    @property
    def service(self) -> BaseProps[Service]:
        if not self._service:
            self._service = BaseProps(self.ros, "/ip/service", Service)
            self._service._create = False
            self._service._delete = False
        return self._service

    @property
    def setting(self) -> Setting:
        return self.ros.get_as("/ip/setting", Setting)

    @property
    def vrf(self) -> BaseProps[Vrf]:
        if not self._vrf:
            self._vrf = BaseProps(self.ros, "/ip/vrf", Vrf)
        return self._vrf


__all__ = [
    "Address",
    "ARP",
    "IPModule",
    "Cloud",
    "DHCPClient",
    "DHCPRelay",
    "DHCPServer",
    "DNS",
    "KidControl",
    "Route",
    "Service",
    "Setting",
    "Vrf",
]
