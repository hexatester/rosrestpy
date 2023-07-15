from attr import dataclass
from typing import Union


@dataclass
class Nexthop:
    id: str
    address: str
    afi: str
    scope: int
    target_scope: int
    gw_check_ok: bool
    interface_ok: bool
    bgp_vpn: bool
    immediate_gwweight: Union[str, int]
    immediate_gwflap_count: Union[str, int]
    immediate_gwinterface_idx: Union[str, int]
    immediate_gwmpls_peer_id: Union[str, int]
    immediate_gwmpls_label: Union[str, int]
    immediate_gwblackhole: bool
    reachable: bool
    unresolved: bool
    immediate_gw_address: str = None
    check_gateway: str = None
