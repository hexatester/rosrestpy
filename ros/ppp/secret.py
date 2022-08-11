from attr import dataclass
from typing import Optional

from ._literals import PPPService


@dataclass
class PPPSecret:
    id: str
    caller_id: str
    disabled: bool
    ipv6_routes: str
    last_logged_out: str
    limit_bytes_in: int
    limit_bytes_out: int
    name: str
    password: str
    profile: str
    routes: str
    service: PPPService
    comment: Optional[str] = None
    local_address: Optional[str] = None
    remote_address: Optional[str] = None
    remote_ipv6_prefix: Optional[str] = None
