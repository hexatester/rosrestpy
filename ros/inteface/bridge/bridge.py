from attr import dataclass
from typing import Optional


@dataclass
class Bridge:
    id: str
    actual_mtu: int
    ageing_time: str
    arp: str
    arp_timeout: str
    auto_mac: bool
    dhcp_snooping: bool
    disabled: bool
    fast_forward: bool
    forward_delay: str
    igmp_snooping: bool
    l2mtu: int
    mac_address: str
    max_message_age: str
    mtu: str
    name: str
    priority: str
    protocol_mode: str
    running: bool
    transmit_hold_count: int
    vlan_filtering: bool
    comment: Optional[str] = None

    def __str__(self) -> str:
        return self.name
