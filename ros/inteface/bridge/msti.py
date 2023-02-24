from attr import dataclass
from typing import Optional


@dataclass
class BridgeMsti:
    bridge: str
    disabled: bool
    identifier: int
    priority: str
    vlan_mapping: int
    id: str
    comment: Optional[str] = None

    def __bool__(self) -> bool:
        return not self.disabled
