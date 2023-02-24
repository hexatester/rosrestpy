from attr import dataclass
from typing import Optional


@dataclass
class BridgeVlan:
    bridge: str
    current_tagged: str
    current_untagged: str
    disabled: bool
    dynamic: bool
    tagged: str
    untagged: str
    vlan_ids: int
    id: str
    comment: Optional[str] = None

    def __bool__(self) -> bool:
        return not self.disabled
