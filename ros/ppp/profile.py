from attr import dataclass
from typing import Optional

from ._literals import YesNoDefault, YesNoDefaultRequired


@dataclass
class PPPProfile:
    id: str
    address_list: str
    bridge_learning: YesNoDefault
    change_tcp_mss: YesNoDefault
    default: bool
    name: str
    on_down: str
    on_up: str
    only_one: YesNoDefault
    use_compression: YesNoDefault
    use_encryption: YesNoDefaultRequired
    use_ipv6: YesNoDefaultRequired
    use_mpls: YesNoDefaultRequired
    use_upnp: YesNoDefault
    bridge: Optional[str] = None
    bridge_horizon: Optional[int] = None
    bridge_path_cost: Optional[int] = None
    bridge_port_priority: Optional[str] = None
    comment: Optional[str] = None
    dhcpv6_pd_pool: Optional[str] = None
    dns_server: Optional[str] = None
    idle_timeout: Optional[str] = None
    incoming_filter: Optional[str] = None
    insert_queue_before: Optional[str] = None
    interface_list: Optional[str] = None
    local_address: Optional[str] = None
    outgoing_filter: Optional[str] = None
    parent_queue: Optional[str] = None
    queue_type: Optional[str] = None
    rate_limit: Optional[str] = None
    remote_address: Optional[str] = None
    remote_ipv6_prefix_pool: Optional[str] = None
    session_timeout: Optional[str] = None
    wins_server: Optional[str] = None

    def __str__(self) -> str:
        return self.name
