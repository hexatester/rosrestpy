from attr import dataclass


@dataclass
class Veth:
    name: str
    address: str
    gateway: str
    comment: str = None
    disabled: bool = False
    copy_from: str = None

    def __str__(self) -> str:
        return self.name
