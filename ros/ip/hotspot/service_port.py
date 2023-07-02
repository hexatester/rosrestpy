from attr import dataclass


@dataclass
class HotspotServicePort:
    id: str
    name: str
    ports: str
    disabled: bool

    def __str__(self) -> str:
        return self.name
