from attr import dataclass


@dataclass
class User:
    name: str
    group: str
    address: str
    disabled: bool
    expired: bool = False
    id: str = None
    last_logged_in: str = None

    def __str__(self) -> str:
        return self.name
