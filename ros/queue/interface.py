from attr import dataclass


@dataclass
class InterfaceQueue:
    id: str
    active_queue: str
    default_queue: str
    interface: str
    queue: str
