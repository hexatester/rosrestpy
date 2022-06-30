from attr import dataclass


@dataclass(slots=True)
class Log:
    id: str
    message: str
    time: str
    topics: str
