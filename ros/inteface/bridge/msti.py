from attr import dataclass


@dataclass
class BridgeMsti:
    bridge: str
    disabled: bool
    identifier: int
    priority: str
    vlan_mapping: int
    comment: str = None
    id: str = None

    def __bool__(self) -> bool:
        return not self.disabled
