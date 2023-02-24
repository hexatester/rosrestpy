from attr import dataclass, field
from typing import Literal, Optional

AddDefaultRoute = Literal["yes", "no", "special-classless"]
Status = Literal[
    "bound", "error", "rebinding...", "requesting...", "searching...", "stopped"
]


@dataclass
class DHCPClient:
    interface: str
    add_default_route: AddDefaultRoute = "yes"
    dhcp_options: str = "hostname,clientid"
    disabled: bool = False
    use_peer_dns: bool = True
    use_peer_ntp: bool = True
    default_route_distance: int = 1
    comment: Optional[str] = None
    address: Optional[str] = None
    dhcp_server: Optional[str] = field(on_setattr=None, default=None)
    expires_after: Optional[str] = field(on_setattr=None, default=None)
    gateway: Optional[str] = field(on_setattr=None, default=None)
    primary_dns: Optional[str] = field(on_setattr=None, default=None)
    primary_ntp: Optional[str] = field(on_setattr=None, default=None)
    secondary_dns: Optional[str] = field(on_setattr=None, default=None)
    status: Status = field(on_setattr=None, default=None)
    dynamic: bool = field(on_setattr=None, default=None)
    invalid: bool = field(on_setattr=None, default=None)
    id: str = field(on_setattr=None, default=None)

    def __str__(self) -> str:
        return self.interface

    def __bool__(self) -> bool:
        return not self.disabled
