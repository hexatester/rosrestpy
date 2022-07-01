from attr import dataclass


@dataclass
class DNS:
    allow_remote_requests: bool
    cache_max_ttl: str
    cache_size: int
    cache_used: int
    dynamic_servers: str
    max_concurrent_queries: int
    max_concurrent_tcp_sessions: int
    max_udp_packet_size: int
    query_server_timeout: str
    query_total_timeout: str
    servers: str
    use_doh_server: str
    verify_doh_cert: bool
