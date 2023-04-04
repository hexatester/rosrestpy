from attr import dataclass, field
from typing import Literal


@dataclass
class Route:
    dst_address: str
    gateway: str
    routing_table: str
    check_gateway: Literal["arp", "bfd", "bfd-multihop", "none", "ping"] = None
    suppress_hw_offload: bool = False
    distance: int = 1
    scope: int = 30
    target_scope: int = None
    vrf_interface: str = None
    pref_src: str = None
    vpn: bool = None
    comment: str = None
    disabled: bool = None
    immediate_gw: str = field(on_setattr=None, default=None)
    active: bool = field(on_setattr=None, default=None)
    dynamic: bool = field(on_setattr=None, default=None)
    ecmp: bool = field(on_setattr=None, default=None)
    hw_offloaded: bool = field(on_setattr=None, default=None)
    inactive: bool = field(on_setattr=None, default=None)
    static: bool = field(on_setattr=None, default=None)
    filtered: bool = field(on_setattr=None, default=None)
    id: str = field(on_setattr=None, default=None)

    def __bool__(self) -> bool:
        return not self.disabled
