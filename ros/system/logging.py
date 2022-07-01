from attr import dataclass


@dataclass
class Logging:
    id: str
    action: str
    default: bool
    disabled: bool
    invalid: bool
    prefix: str
    topics: str
