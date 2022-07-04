from attr import dataclass


@dataclass(slots=True)
class Traceroute:
    section: int
    address: str
    avg: float
    best: float
    last: str
    loss: float
    sent: int
    status: str
    std_dev: float
    worst: float

    def __str__(self) -> str:
        return self.address
