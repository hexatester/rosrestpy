from attr import dataclass
from typing import Optional


@dataclass
class BridgeVlan:
    id: str
    bridge: str
    current_tagged: str
    current_untagged: str
    disabled: bool
    dynamic: bool
    tagged: str
    untagged: str
    vlan_ids: int
    comment: Optional[str] = None
