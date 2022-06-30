from attr import dataclass
from datetime import time


@dataclass(slots=True)
class Log:
    id: str
    message: str
    time: time
    topics: str
