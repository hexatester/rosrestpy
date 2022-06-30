from typing import List
from ros.base import BaseModule

from .address import Address
from .arp import ARP


class IP(BaseModule):
    @property
    def address(self) -> List[Address]:
        return self.ros.get_as(self.url + "/address", List[Address])

    @property
    def arp(self) -> List[ARP]:
        return self.ros.get_as(self.url + "/arp", List[ARP])


__all__ = ["Address", "ARP", "IP"]
