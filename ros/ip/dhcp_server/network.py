from attr import dataclass


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
    dhcp_option_set: str = None
    domain: str = None
    next_server: str = None
    boot_file_name: str = None
    netmask: int = None
    comment: str = None
    id: str = None
