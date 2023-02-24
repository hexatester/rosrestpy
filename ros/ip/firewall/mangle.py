from attr import dataclass
from typing import Literal, Optional

from ._literals import IPv4Options

Action = Literal[
    "accept",
    "add-dst-to-address-list",
    "add-src-to-address-list",
    "change-dscp",
    "change-mss",
    "change-ttl",
    "clear-df",
    "fasttrack-connection",
    "jump",
    "log",
    "mark-connection",
    "mark-packet",
    "mark-routing",
    "passthrough",
    "return",
    "route",
    "set-priority",
    "sniff-pc",
    "sniff-tzsp",
    "strip-ipv4-options",
    "return",
    "route",
    "set-priority",
    "sniff-pc",
    "sniff-tzsp",
    "strip-ipv4-options",
]


@dataclass
class IPFirewallMangle:
    # General
    chain: str
    src_address: Optional[str] = None
    dst_address: Optional[str] = None
    src_address_list: Optional[str] = None
    dst_address_list: Optional[str] = None
    protocol: Optional[str] = None
    src_port: Optional[str] = None
    dst_port: Optional[str] = None
    port: Optional[str] = None
    in_interface: Optional[str] = None
    out_interface: Optional[str] = None
    in_interface_list: Optional[str] = None
    out_interface_list: Optional[str] = None
    packet_mark: Optional[str] = None
    connection_mark: Optional[str] = None
    routing_mark: Optional[str] = None
    connection_type: Optional[str] = None
    connection_state: Optional[str] = None
    connection_nat_state: Optional[str] = None
    # Advanced
    layer7_protocol: Optional[str] = None
    content: Optional[str] = None
    connection_bytes: Optional[str] = None
    connection_rate: Optional[str] = None
    per_connection_classifier: Optional[str] = None
    src_mac_address: Optional[str] = None
    out_bridge_port: Optional[str] = None
    in_bridge_port: Optional[str] = None
    out_bridge_port_list: Optional[str] = None
    in_bridge_port_list: Optional[str] = None
    ipsec_policy: Optional[str] = None
    tls_host: Optional[str] = None
    ingress_priority: Optional[str] = None
    priority: Optional[str] = None
    dscp: Optional[str] = None
    tcp_mss: Optional[str] = None
    packet_size: Optional[str] = None
    random: Optional[int] = None
    tcp_flags: Optional[str] = None
    icmp_options: Optional[str] = None
    ipv4_options: Optional[IPv4Options] = None
    ttl: Optional[str] = None
    # Extra
    nth: Optional[str] = None
    connection_limit: Optional[str] = None
    src_address_type: Optional[str] = None
    dst_address_type: Optional[str] = None
    hotspot: Optional[str] = None
    fragment: Optional[bool] = None
    limit: Optional[str] = None
    dst_limit: Optional[str] = None
    time: Optional[str] = None
    psd: Optional[str] = None
    # Action
    action: Action = "accept"
    log: Optional[bool] = None
    log_prefix: Optional[str] = None
    address_list: Optional[str] = None
    address_list_timeout: Optional[str] = None
    new_connection_mark: Optional[str] = None
    new_dscp: Optional[str] = None
    new_mss: Optional[str] = None
    new_packet_mark: Optional[str] = None
    new_priority: Optional[str] = None
    new_routing_mark: Optional[str] = None
    new_ttl: Optional[str] = None
    jump_target: Optional[str] = None
    passthrough: Optional[bool] = None
    route_dst: Optional[str] = None
    sniff_id: Optional[str] = None
    sniff_target: Optional[str] = None
    sniff_target_port: Optional[str] = None
    # Statistics
    bytes: int = None
    packets: int = None
    # Etc
    id: str = None
    disabled: Optional[str] = None
    comment: Optional[str] = None
    copy_from: Optional[str] = None
    place_before: Optional[str] = None
    p2p: str = None
    realm: str = None

    def __bool__(self) -> bool:
        return not self.disabled
