from attr import dataclass

from ._literals import DNSType


@dataclass(slots=True)
class DNSCache:
    id: str
    name: str
    static: bool
    ttl: str
    type: DNSType
    data: str = None
