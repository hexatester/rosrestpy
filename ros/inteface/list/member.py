from attr import dataclass
from typing import Optional


@dataclass
class InterfaceListMember:
    interface: str
    list: str
    disabled: bool
    dynamic: bool
    id: str
    comment: Optional[str] = None

    def __bool__(self) -> bool:
        return not self.disabled
