from attr import dataclass
from typing import Literal


Scheduled = Literal[
    "scheduled for disable", "scheduled for enable", "scheduled for uninstall", ""
]


@dataclass
class Package:
    id: str
    build_time: str
    disabled: bool
    name: str
    version: str
    scheduled: Scheduled
