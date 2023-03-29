from attr import dataclass


@dataclass
class UserGroup:
    policy: str
    name: str
    skin: str = "default"
    id: str = None

    def __str__(self) -> str:
        return self.name
