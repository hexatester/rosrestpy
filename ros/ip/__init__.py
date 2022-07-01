from typing import List
from ros.base import BaseModule

from .address import Address
from .arp import ARP
from .cloud import Cloud
from .dhcp_client import DHCPClient


class IP(BaseModule):
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


__all__ = ["Address", "ARP", "IP", "Cloud", "DHCPClient"]
