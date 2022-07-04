from attr import dataclass


@dataclass(slots=True)
class Health:
    id: str
    name: str
    type: str
    value: float
