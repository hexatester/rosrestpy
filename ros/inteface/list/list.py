from attr import dataclass
from typing import Optional


@dataclass
class InterfaceList:
    name: str
    exclude: str
    include: str
    builtin: bool
    dynamic: bool
    id: str = None
    comment: Optional[str] = None

    def __str__(self) -> str:
        return self.name
