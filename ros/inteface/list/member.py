from attr import dataclass


@dataclass
class InterfaceListMember:
    interface: str
    list: str
    disabled: bool
    dynamic: bool
    comment: str = None
    id: str = None

    def __bool__(self) -> bool:
        return not self.disabled
