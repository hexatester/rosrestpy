from attr import dataclass
from typing import Optional


@dataclass
class InterfaceListMember:
    id: str
    disabled: bool
    dynamic: bool
    interface: str
    list: str
    comment: Optional[str] = None
