from attr import dataclass
from typing import Optional


@dataclass
class BridgeMsti:
    id: str
    bridge: str
    disabled: bool
    identifier: int
    priority: str
    vlan_mapping: int
    comment: Optional[str] = None
