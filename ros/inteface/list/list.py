from attr import dataclass
from typing import Optional


@dataclass
class InterfaceList:
    id: str
    builtin: bool
    dynamic: bool
    exclude: str
    include: str
    name: str
    comment: Optional[str] = None

    def __str__(self) -> str:
        return self.name
