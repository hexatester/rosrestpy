from attr import dataclass
from typing import Optional


@dataclass
class DHCPNetwork:
    id: str
    address: str
    caps_manager: str
    dhcp_option: str
    dns_server: str
    dynamic: bool
    gateway: str
    ntp_server: str
    wins_server: str
    comment: Optional[str] = None
