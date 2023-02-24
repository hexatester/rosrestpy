from attr import dataclass


@dataclass
class InterfaceQueue:
    interface: str
    queue: str
    active_queue: str
    default_queue: str
    id: str
