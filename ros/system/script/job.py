from attr import dataclass


@dataclass
class Job:
    id: str
    owner: str
    policy: str
    started: str
    type: str
    nextid: str = None
    parent: str = None
