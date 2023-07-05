from attr import dataclass
from typing import Literal
from ros._literals import ARPLiteral


@dataclass
class Vrrp:
    name: str
    interface: str
    mtu: int = 1500
    arp: ARPLiteral = "enabled"
    arp_timeout: str = None
    vrid: int = 1
    priority: int = 100
    group_authority: str = "none"
    interval: str = "1.00"
    preemption_mode: bool = True
    authentication: Literal["none", "simple", "ah"] = "none"
    version: Literal["2", "3"] = "2"
    v3_protocol: Literal["ipv4", "ipv6"] = "ipv4"
    sync_connection_tracking: bool = False
    remote_address: str = None
    password: str = None
    on_master: str = None
    on_backup: str = None
    on_fail: str = None
    comment: str = None
    disabled: bool = None
    copy_from: str = None
    id: str = None
    grp_member: bool = None
    mac_address: str = None
    running: bool = None
    invalid: bool = None

    def __str__(self) -> str:
        return self.name
