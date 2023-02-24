from attr import dataclass, field
from typing import Optional


@dataclass
class ARP:
    address: str
    interface: str
    mac_address: Optional[str] = None
    published: bool = False
    disabled: bool = False
    comment: Optional[str] = None
    id: str = field(on_setattr=None, default=None)
    DHCP: Optional[bool] = field(on_setattr=None, default=None)
    complete: Optional[bool] = field(on_setattr=None, default=None)
    dynamic: Optional[bool] = field(on_setattr=None, default=None)
    invalid: Optional[bool] = field(on_setattr=None, default=None)

    def __bool__(self) -> bool:
        return not self.disabled
