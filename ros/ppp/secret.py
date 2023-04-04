from attr import dataclass

from ._literals import PPPService


@dataclass
class PPPSecret:
    name: str
    profile: str
    id: str = None
    caller_id: str = None
    disabled: bool = False
    ipv6_routes: str = None
    last_logged_out: str = None
    limit_bytes_in: int = None
    limit_bytes_out: int = None
    password: str = None
    routes: str = None
    service: PPPService = "any"
    comment: str = None
    local_address: str = None
    remote_address: str = None
    remote_ipv6_prefix: str = None

    def __str__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return not self.disabled
