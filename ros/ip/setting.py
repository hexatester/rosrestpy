from attr import dataclass


@dataclass
class Setting:
    accept_redirects: bool
    accept_source_route: bool
    allow_fast_path: bool
    arp_timeout: str
    icmp_rate_limit: int
    icmp_rate_mask: str
    ip_forward: bool
    ipv4_fast_path_active: bool
    ipv4_fast_path_bytes: int
    ipv4_fast_path_packets: int
    ipv4_fasttrack_active: bool
    ipv4_fasttrack_bytes: int
    ipv4_fasttrack_packets: int
    max_neighbor_entries: int
    route_cache: bool
    rp_filter: str
    secure_redirects: bool
    send_redirects: bool
    tcp_syncookies: bool
