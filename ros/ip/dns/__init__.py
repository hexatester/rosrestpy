from attr import dataclass
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ros.ros import Ros

from .cache import DNSCache
from .static import DNSStatic


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
    _ros: Optional["Ros"] = None

    def cache(self, **kwds) -> List[DNSCache]:
        assert self._ros
        return self._ros.get_as("/ip/dns/cache", List[DNSCache], kwds)

    def static(self, **kwds) -> List[DNSStatic]:
        assert self._ros
        return self._ros.get_as("/ip/dns/static", List[DNSStatic], kwds)

    def flush(self):
        assert self._ros
        self._ros.post_as("/ip/dns/cache/flush", List[DNSCache])


__all__ = ["DNSCache", "DNS", "DNSStatic"]
