from attr import dataclass, field


@dataclass
class ARP:
    address: str
    interface: str
    mac_address: str = None
    published: bool = False
    disabled: bool = False
    comment: str = None
    id: str = field(on_setattr=None, default=None)
    DHCP: bool = field(on_setattr=None, default=None)
    complete: bool = field(on_setattr=None, default=None)
    dynamic: bool = field(on_setattr=None, default=None)
    invalid: bool = field(on_setattr=None, default=None)

    def __bool__(self) -> bool:
        return not self.disabled
