from attr import dataclass, field
from typing import Literal

AddDefaultRoute = Literal["yes", "no", "special-classless"]
Status = Literal[
    "bound",
    "error",
    "rebinding...",
    "requesting...",
    "searching...",
    "stopped",
    "renewing...",
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
    comment: str = None
    address: str = None
    dhcp_server: str = field(on_setattr=None, default=None)
    expires_after: str = field(on_setattr=None, default=None)
    gateway: str = field(on_setattr=None, default=None)
    primary_dns: str = field(on_setattr=None, default=None)
    primary_ntp: str = field(on_setattr=None, default=None)
    secondary_dns: str = field(on_setattr=None, default=None)
    status: Status = field(on_setattr=None, default=None)
    dynamic: bool = field(on_setattr=None, default=None)
    invalid: bool = field(on_setattr=None, default=None)
    id: str = field(on_setattr=None, default=None)

    def __str__(self) -> str:
        return self.interface

    def __bool__(self) -> bool:
        return not self.disabled
