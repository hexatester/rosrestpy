from attr import dataclass
from typing import Optional

from ros._literals import ARPLiteral


@dataclass
class Bridge:
    name: str
    arp: ARPLiteral
    ageing_time: str
    arp_timeout: str
    auto_mac: bool
    dhcp_snooping: bool
    disabled: bool
    fast_forward: bool
    forward_delay: str
    igmp_snooping: bool
    mac_address: str
    max_message_age: str
    mtu: str
    priority: str
    protocol_mode: str
    running: bool
    transmit_hold_count: int
    vlan_filtering: bool
    id: str
    actual_mtu: Optional[int] = None
    l2mtu: Optional[int] = None
    comment: Optional[str] = None

    def __str__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return not self.disabled
