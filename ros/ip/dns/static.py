from attr import dataclass

from ._literals import DNSType


@dataclass
class DNSStatic:
    id: str
    disabled: bool
    ttl: str
    dynamic: bool = False
    address: str = None
    cname: str = None
    comment: str = None
    forward_to: str = None
    ipv6_address: str = None
    name: str = None
    ns: str = None
    mx_preference: str = None
    mx_exchange: str = None
    regexp: str = None
    srv_priority: int = None
    srv_weight: int = None
    srv_port: int = None
    srv_target: str = None
    text: str = None
    type: DNSType = None

    def __bool__(self) -> bool:
        return not self.disabled
