from attr import dataclass
from typing import Optional


@dataclass
class ARP:
    id: str
    DHCP: bool
    address: str
    complete: bool
    disabled: bool
    dynamic: bool
    interface: str
    invalid: bool
    published: bool
    mac_address: Optional[str] = None
    comment: Optional[str] = None
