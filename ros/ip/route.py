from typing import Optional
from attr import dataclass


@dataclass
class Route:
    id: str
    distance: int
    dst_address: str
    dynamic: bool
    ecmp: bool
    gateway: str
    hw_offloaded: bool
    immediate_gw: str
    inactive: bool
    routing_table: str
    scope: int
    suppress_hw_offload: bool
    active: bool = False
    pref_src: Optional[str] = None
    target_scope: Optional[int] = None
    vpn: Optional[bool] = None
    vrf_interface: Optional[str] = None
    comment: Optional[str] = None
