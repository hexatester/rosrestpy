from attr import dataclass
from typing import Any


@dataclass(slots=True)
class History:
    id: str
    action: str
    by: str
    policy: str
    redo: str
    undoable: bool
