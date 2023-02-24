from attr import dataclass, field
from typing import Optional


@dataclass
class DHCPLease:
    # General
    address: str
    mac_address: Optional[str] = None
    use_src_mac: bool = False
    client_id: Optional[str] = None
    server: str = "all"
    lease_time: Optional[str] = None
    block_access: bool = False
    allow_dual_stack_queue: bool = True
    always_broadcast: bool = False
    dhcp_option: Optional[str] = None
    dhcp_option_set: Optional[str] = None
    rate_limit: Optional[str] = None
    parent_queue: Optional[str] = None
    queue_type: Optional[str] = None
    routes: Optional[str] = None
    insert_queue_before: Optional[str] = None
    address_lists: Optional[str] = None
    comment: Optional[str] = None
    disabled: bool = False
    copy_from: Optional[str] = None
    # Active
    active_address: str = field(on_setattr=None, default=None)
    active_client_id: str = field(on_setattr=None, default=None)
    active_mac_address: str = field(on_setattr=None, default=None)
    active_server: str = field(on_setattr=None, default=None)
    blocked: bool = field(on_setattr=None, default=None)
    dynamic: bool = field(on_setattr=None, default=None)
    expires_after: str = field(on_setattr=None, default=None)
    host_name: str = field(on_setattr=None, default=None)
    last_seen: str = field(on_setattr=None, default=None)
    radius: str = field(on_setattr=None, default=None)
    status: str = field(on_setattr=None, default=None)

    def __bool__(self) -> bool:
        return not self.disabled
