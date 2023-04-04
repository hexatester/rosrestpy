from attr import dataclass, field


@dataclass
class DHCPLease:
    # General
    address: str
    mac_address: str = None
    use_src_mac: bool = False
    client_id: str = None
    server: str = "all"
    lease_time: str = None
    block_access: bool = False
    allow_dual_stack_queue: bool = True
    always_broadcast: bool = False
    dhcp_option: str = None
    dhcp_option_set: str = None
    rate_limit: str = None
    parent_queue: str = None
    queue_type: str = None
    routes: str = None
    insert_queue_before: str = None
    address_lists: str = None
    comment: str = None
    disabled: bool = False
    copy_from: str = None
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
