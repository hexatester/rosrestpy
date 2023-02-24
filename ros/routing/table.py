from attr import dataclass
from typing import Optional


@dataclass(slots=True)
class RoutingTable:
    id: str
    name: str
    invalid: bool
    dynamic: bool = False
    fib: str = "no"
    comment: Optional[str] = None

    def __str__(self) -> str:
        return self.name

    def __attrs_post_init__(self):
        if self.fib == "":
            self.fib = "yes"
