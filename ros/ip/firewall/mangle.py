from attr import dataclass
from typing import Literal

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
    src_address: str = None
    dst_address: str = None
    src_address_list: str = None
    dst_address_list: str = None
    protocol: str = None
    src_port: str = None
    dst_port: str = None
    port: str = None
    in_interface: str = None
    out_interface: str = None
    in_interface_list: str = None
    out_interface_list: str = None
    packet_mark: str = None
    connection_mark: str = None
    routing_mark: str = None
    connection_type: str = None
    connection_state: str = None
    connection_nat_state: str = None
    # Advanced
    layer7_protocol: str = None
    content: str = None
    connection_bytes: str = None
    connection_rate: str = None
    per_connection_classifier: str = None
    src_mac_address: str = None
    out_bridge_port: str = None
    in_bridge_port: str = None
    out_bridge_port_list: str = None
    in_bridge_port_list: str = None
    ipsec_policy: str = None
    tls_host: str = None
    ingress_priority: str = None
    priority: str = None
    dscp: str = None
    tcp_mss: str = None
    packet_size: str = None
    random: int = None
    tcp_flags: str = None
    icmp_options: str = None
    ipv4_options: IPv4Options = None
    ttl: str = None
    # Extra
    nth: str = None
    connection_limit: str = None
    src_address_type: str = None
    dst_address_type: str = None
    hotspot: str = None
    fragment: bool = None
    limit: str = None
    dst_limit: str = None
    time: str = None
    psd: str = None
    # Action
    action: Action = "accept"
    log: bool = None
    log_prefix: str = None
    address_list: str = None
    address_list_timeout: str = None
    new_connection_mark: str = None
    new_dscp: str = None
    new_mss: str = None
    new_packet_mark: str = None
    new_priority: str = None
    new_routing_mark: str = None
    new_ttl: str = None
    jump_target: str = None
    passthrough: bool = None
    route_dst: str = None
    sniff_id: str = None
    sniff_target: str = None
    sniff_target_port: str = None
    # Statistics
    bytes: int = None
    packets: int = None
    # Etc
    id: str = None
    disabled: str = None
    comment: str = None
    copy_from: str = None
    place_before: str = None
    p2p: str = None
    realm: str = None

    def __bool__(self) -> bool:
        return not self.disabled
