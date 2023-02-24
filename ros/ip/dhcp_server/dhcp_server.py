from attr import dataclass
from typing import Optional, Union, Literal

from ._literals import Authoritative, UseRadius


@dataclass
class DHCPServer:
    name: str
    interface: str
    address_pool: str = "static-only"
    lease_time: str = "00:10:00"
    authoritative: Authoritative = "yes"
    disabled: bool = False
    use_radius: UseRadius = "no"
    always_broadcast: bool = False
    add_arp: bool = False
    conflict_detection: bool = True
    use_framed_as_classless: bool = True
    use_radius: bool = "no"
    lease_script: Optional[str] = None
    insert_queue_before: str = "first"
    parent_queue: Optional[str] = None
    allow_dual_stack_queue: bool = True
    comment: Optional[str] = None
    relay: Optional[str] = None
    client_mac_limit: Optional[str] = None
    bootp_lease_time: str = "forever"
    delay_threshold: Optional[str] = None
    dhcp_option_set: Optional[str] = None
    server_address: Optional[str] = None
    bootp_support: Optional[Literal["dynamic", "static"]] = None
    invalid: Optional[bool] = None
    dynamic: Optional[bool] = None
    id: str = None

    def __str__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return not self.disabled
