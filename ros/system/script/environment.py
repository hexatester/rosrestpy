from attr import dataclass


@dataclass
class Environment:
    name: str
    value: str = None
    id: str = None
