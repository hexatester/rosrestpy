from attr import dataclass
from typing import List

from ros._base import BM

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
    _mod: BM = None

    def cache(self, **kwds) -> List[DNSCache]:
        assert self._mod is not None
        return self._mod.ros.get_as(self._mod.url + "/dns/cache", List[DNSCache], kwds)

    def static(self, **kwds) -> List[DNSStatic]:
        assert self._mod is not None
        return self._mod.ros.get_as(
            self._mod.url + "/dns/static", List[DNSStatic], kwds
        )

    def flush(self):
        assert self._mod is not None
        self._mod.ros.post_as(self._mod.url + "/dns/cache/flush", List[DNSCache])


__all__ = ["DNSCache", "DNS", "DNSStatic"]
