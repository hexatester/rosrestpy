from typing import Optional
from attr import dataclass

from ._literals import DNSType


@dataclass
class DNSStatic:
    id: str
    disabled: bool
    ttl: str
    dynamic: bool = False
    address: Optional[str] = None
    cname: Optional[str] = None
    comment: Optional[str] = None
    forward_to: Optional[str] = None
    ipv6_address: Optional[str] = None
    name: Optional[str] = None
    ns: Optional[str] = None
    mx_preference: Optional[str] = None
    mx_exchange: Optional[str] = None
    regexp: Optional[str] = None
    srv_priority: Optional[int] = None
    srv_weight: Optional[int] = None
    srv_port: Optional[int] = None
    srv_target: Optional[str] = None
    text: Optional[str] = None
    type: Optional[DNSType] = None

    def __bool__(self) -> bool:
        return not self.disabled
