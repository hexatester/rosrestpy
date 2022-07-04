from attr import dataclass


@dataclass
class InterfaceListMember:
    id: str
    disabled: bool
    dynamic: bool
    interface: str
    list: str
