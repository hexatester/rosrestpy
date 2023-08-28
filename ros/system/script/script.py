from attr import dataclass


@dataclass
class Script:
    name: str
    source: str
    dont_require_permissions: bool
    policy: str
    comment: str = None
    id: str = None
    nextid: str = None
    copy_from: str = None
    owner: str = None
    run_count: int = None
    last_started: str = None
    invalid: bool = None
