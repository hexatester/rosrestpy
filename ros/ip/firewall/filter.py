from attr import dataclass


@dataclass
class IPFirewallFilter:
    # General
    chain: str
    src_address: str
    dst_address: str
    src_address_list: str
    dst_address_list: str
    protocol: str
    src_port: str
    dst_port: str
    port: str
    in_interface: str
    out_interface: str
    in_interface_list: str
    out_interface_list: str
    packet_mark: str
    connection_mark: str
    routing_mark: str
    connection_type: str
    connection_state: str
    connection_nat_state: str
    disabled: str
    comment: str
    # Advanced
    layer7_protocol: str
    content: str
    connection_bytes: str
    connection_rate: str
    per_connection_classifier: str
    src_mac_address: str
    out_bridge_port: str
    in_bridge_port: str
    out_bridge_port_list: str
    in_bridge_port_list: str
    ipsec_policy: str
    tls_host: str
    ingress_priority: str
    priority: str
    dscp: str
    tcp_mss: str
    packet_size: str
    random: str
    tcp_flags: str
    icmp_options: str
    ipv4_options: str
    ttl: str
    # Extra
    nth: str
    connection_limit: str
    src_address_type: str
    dst_address_type: str
    hotspot: str
    fragment: str
    limit: str
    dst_limit: str
    time: str
    psd: str
    # Action
    action: str
    log: str
    log_prefix: str
    address_list: str
    address_list_timeout: str
    jump_target: str
    reject_with: str
    # Etc
    copy_from: str = None
    place_before: str = None
    p2p: str = None
    hw_offload: str = None
    realm: str = None
