from attr import dataclass


@dataclass
class UserActive:
    id: str
    group: str
    name: str
    radius: bool
    via: str
    when: str
    address: str = None
