from attr import dataclass
from typing import Optional

from ._literals import PPPService


@dataclass
class PPPSecret:
    name: str
    profile: str
    id: str = None
    caller_id: Optional[str] = None
    disabled: bool = False
    ipv6_routes: Optional[str] = None
    last_logged_out: Optional[str] = None
    limit_bytes_in: Optional[int] = None
    limit_bytes_out: Optional[int] = None
    password: Optional[str] = None
    routes: Optional[str] = None
    service: PPPService = "any"
    comment: Optional[str] = None
    local_address: Optional[str] = None
    remote_address: Optional[str] = None
    remote_ipv6_prefix: Optional[str] = None

    def __str__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return not self.disabled
