from attr import dataclass
from typing import Optional


@dataclass
class DHCPClient:
    id: str
    add_default_route: str
    dhcp_options: str
    disabled: bool
    dynamic: bool
    interface: str
    invalid: bool
    use_peer_dns: bool
    use_peer_ntp: bool
    address: Optional[str] = None
    comment: Optional[str] = None
    default_route_distance: Optional[int] = None
    dhcp_server: Optional[str] = None
    expires_after: Optional[str] = None
    gateway: Optional[str] = None
    primary_dns: Optional[str] = None
    primary_ntp: Optional[str] = None
    secondary_dns: Optional[str] = None
    status: Optional[str] = None

    def __str__(self) -> str:
        return self.interface
