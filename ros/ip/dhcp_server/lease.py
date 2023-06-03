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
    # Active
    active_address: str = None
    active_client_id: str = None
    active_mac_address: str = None
    active_server: str = None
    blocked: bool = None
    dynamic: bool = None
    expires_after: str = None
    host_name: str = None
    last_seen: str = None
    radius: str = None
    status: str = None
    id: str = None
    copy_from: str = None

    def __bool__(self) -> bool:
        return not self.disabled
