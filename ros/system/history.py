from attr import dataclass


@dataclass(slots=True)
class History:
    id: str
    action: str
    by: str
    policy: str
    redo: str
    undoable: bool

    def __str__(self) -> str:
        return self.action
