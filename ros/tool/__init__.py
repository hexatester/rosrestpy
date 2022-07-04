from typing import List

from ros._base import BaseModule

from .bandwith_test import BandwithTest
from .ping import Ping
from .traceroute import Traceroute


class ToolModule(BaseModule):
    def ping(self, address: str, count: int = 4):
        data = {"address": address, "count": count}
        return self.ros.post_as("/ping", List[Ping], data)

    def bandwith_test(
        self,
        address: str,
        duration: str,
        user: str = None,
        password: str = None,
        protocol: str = "udp",
        direction: str = "receive",
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


__all__ = ["BandwithTest", "Ping", "ToolModule", "Traceroute"]
