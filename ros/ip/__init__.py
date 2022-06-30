from typing import List
from ros.base import BaseModule

from .arp import ARP


class IP(BaseModule):
    @property
    def arp(self) -> List[ARP]:
        return self.ros.get_as(self.url + "/arp", List[ARP])


__all__ = ["ARP", "IP"]
