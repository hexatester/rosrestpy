from attr import dataclass


@dataclass
class Identity:
    name: str

    def __str__(self) -> str:
        return self.name
