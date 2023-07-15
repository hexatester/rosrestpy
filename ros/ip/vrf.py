from attr import dataclass


@dataclass
class Vrf:
    name: str
    interfaces: str
    comment: str = None
    disabled: bool = False
    id: str = None
    builtin: bool = None
    copy_from: str = None
    place_before: str = None

    def __str__(self) -> str:
        return self.name
