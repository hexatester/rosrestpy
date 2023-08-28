from typing import List, Literal, Union

from ros._base import BaseModule, BaseProps
from ros._literals import AnyLiteral, IPProtocol, MACProtocol, PortLiteral

from .bandwith_server import BandwithServer
from .bandwith_test import BandwithTest
from .ip_scan import IPScan
from .netwatch import Netwatch
from .ping import Ping
from .profile import Profile
from .torch import Torch
from .traceroute import Traceroute


class ToolModule(BaseModule):
    _netwatch: BaseProps[Netwatch] = None

    @property
    def bandwith_server(self) -> BandwithServer:
        return self.ros.get_as(self.url + "/bandwidth-server", BandwithServer)

    def ping(
        self,
        address: str,
        count: int = 4,
        interface: str = None,
        arp_ping: bool = False,
        src_address: str = None,
        size: int = 56,
        dscp: int = 0,
        ttl: int = 0,
        vrf: str = "main",
    ):
        data = {
            "address": address,
            "count": count,
            "arp-ping": arp_ping,
            "size": size,
            "dscp": dscp,
            "vrf": vrf,
        }
        if interface:
            data["interface"] = interface
        if src_address:
            data["src-address"] = src_address
        if ttl > 0:
            data["ttl"] = ttl
        return self.ros.post_as("/ping", List[Ping], data)

    def profile(
        self,
        cpu: Literal["total", "all"] = "total",
        duration: str = "5s",
    ) -> List[Profile]:
        data = {"cpu": cpu, "duration": duration}
        return self.ros.post_as("/tool/profile", List[Profile], data)

    def bandwith_test(
        self,
        address: str,
        duration: str,
        user: str = None,
        password: str = None,
        protocol: Literal["tcp", "udp"] = "udp",
        direction: Literal["receive", "send", "both"] = "receive",
        random_data: bool = False,
    ) -> List[BandwithTest]:
        data = {
            "address": address,
            "duration": duration,
            "user": user,
            "password": password,
            "protocol": protocol,
            "direction": direction,
            "random-data": random_data,
        }
        return self.ros.post_as(self.url + "/bandwidth-test", List[BandwithTest], data)

    def ip_scan(
        self,
        interface: str,
        duration: str,
        address_range: str = None,
        freeze_frame_interval: str = None,
    ) -> List[IPScan]:
        data = {"interface": interface, "duration": duration}
        if address_range:
            data["address-range"] = address_range
        if freeze_frame_interval:
            data["freeze-frame-interval"] = freeze_frame_interval
        return self.ros.post_as(self.url + "/ip-scan", List[IPScan], data)

    @property
    def netwatch(self):
        if not self._netwatch:
            self._netwatch = BaseProps(self.ros, "/tool/netwatch", Netwatch)
        return self._netwatch

    def torch(
        self,
        interface: str,
        duration: str = "5s",
        src_address: str = "0.0.0.0/0",
        dst_address: str = "0.0.0.0/0",
        src_address6: str = "::/0",
        dst_address6: str = "::/0",
        mac_protocol: Union[AnyLiteral, MACProtocol] = None,
        port: Union[AnyLiteral, PortLiteral] = None,
        ip_protocol: Union[AnyLiteral, IPProtocol] = None,
        vlan_id: Union[AnyLiteral, int] = None,
        dscp: Union[AnyLiteral, int] = None,
        cpu: str = None,
        freeze_frame_interval: str = None,
    ):
        data = {"interface": interface, "duration": duration}
        if src_address:
            data["src-address"] = src_address
        if dst_address:
            data["dst-address"] = dst_address
        if src_address6:
            data["src-address6"] = src_address6
        if dst_address6:
            data["dst-address6"] = dst_address6
        if mac_protocol:
            data["mac-protocol"] = mac_protocol
        if port:
            data["port"] = port
        if ip_protocol:
            data["ip-protocol"] = ip_protocol
        if vlan_id:
            data["vlan-id"] = vlan_id
        if dscp:
            data["dscp"] = dscp
        if cpu:
            data["cpu"] = cpu
        if freeze_frame_interval:
            data["freeze-frame-interval"] = freeze_frame_interval
        return self.ros.post_as(self.url + "/torch", List[Torch], data)

    def traceroute(
        self,
        address: str,
        duration: str = "5s",
        size: int = 56,
        timeout: str = "1000ms",
        protocol: str = "icmp",
        port: int = "33434",
        use_dns: bool = False,
        count: int = None,
        max_hops: int = None,
        src_address: str = None,
        interface: str = None,
        dscp: int = 0,
        vrf: str = "main",
    ) -> List[Traceroute]:
        data = {
            "address": address,
            "duration": duration,
            "size": size,
            "timeout": timeout,
            "protocol": protocol,
            "port": port,
            "use-dns": use_dns,
            "dscp": dscp,
            "vrf": vrf,
        }
        if count and count > 0:
            data["count"] = count
        if max_hops and max_hops > 0:
            data["max-hops"] = max_hops
        if interface:
            data["interface"] = interface
        if src_address:
            data["src-address"] = src_address
        return self.ros.post_as(self.url + "/traceroute", List[Traceroute], data)

    def torch(
        self,
        interface: str,
        duration: str = "3s",
        src_address: str = "0.0.0.0/0",
        dst_address: str = "0.0.0.0/0",
        src_address6: str = "::/0",
        dst_address6: str = "::/0",
        mac_protocol: Union[AnyLiteral, MACProtocol] = "any",
        ip_protocol: Union[AnyLiteral, IPProtocol] = "any",
        port: PortLiteral = "any",
        vlan_id: Union[AnyLiteral, int] = "any",
        dscp: Union[AnyLiteral, int] = "any",
        cpu: Union[AnyLiteral, int] = "any",
        freeze_frame_interval: str = None,
    ) -> List[Torch]:
        data = {
            "interface": interface,
            "dst-address": dst_address,
            "mac-protocol": mac_protocol,
            "src-address6": src_address6,
            "cpu": cpu,
            "dst-address6": dst_address6,
            "port": port,
            "vlan-id": vlan_id,
            "dscp": dscp,
            "duration": duration,
            "ip-protocol": ip_protocol,
            "src-address": src_address,
        }
        if freeze_frame_interval:
            data["freeze-frame-interval"] = freeze_frame_interval
        return self.ros.post_as(self.url + "/torch", List[Torch], data)

    def wol(self, interface: str, mac: str) -> List[dict]:
        data = {"interface": interface, "mac": mac}
        return self.ros.post_as(self.url + "/wol", List[dict], data)


__all__ = [
    "BandwithServer",
    "BandwithTest",
    "IPScan",
    "Ping",
    "ToolModule",
    "Torch",
    "Traceroute",
]
