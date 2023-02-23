from attr import dataclass
from typing import Optional


@dataclass
class DHCPNetwork:
    address: str
    caps_manager: str
    dhcp_option: str
    dns_server: str
    dynamic: bool
    gateway: str
    ntp_server: str
    wins_server: str
    dns_none: bool = False
    dhcp_option_set: Optional[str] = None
    domain: Optional[str] = None
    next_server: Optional[str] = None
    boot_file_name: Optional[str] = None
    netmask: Optional[int] = None
    comment: Optional[str] = None
    id: str = None
