from attr import dataclass
from typing import Literal

from ros._literals import ARPLiteral

LoopProtectLiteral = Literal["default", "on", "off"]


@dataclass
class Vlan:
    name: str
    vlan_id: int
    interface: str
    arp: ARPLiteral = "enabled"
    mtu: int = 1500
    arp_timeout: str = None
    use_service_tag: bool = False
    loop_protect: LoopProtectLiteral = "default"
    loop_protect_disable_time: str = None
    loop_protect_send_interval: str = None
    comment: str = None
    disabled: bool = False
    copy_from: str = None
    id: str = None
    mac_address: str = None
    l2mtu: int = None
    loop_protect_status: str = None
    running: bool = None

    def __str__(self) -> str:
        return self.name
