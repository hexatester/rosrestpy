from attr import dataclass


@dataclass(slots=True)
class Logging:
    id: str
    action: str
    default: bool
    disabled: bool
    invalid: bool
    prefix: str
    topics: str

    def __bool__(self) -> bool:
        return not self.disabled
