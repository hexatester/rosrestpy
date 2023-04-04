from attr import dataclass


@dataclass
class InterfaceList:
    name: str
    exclude: str
    include: str
    builtin: bool
    dynamic: bool
    comment: str = None
    id: str = None

    def __str__(self) -> str:
        return self.name
