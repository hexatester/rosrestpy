from attr import dataclass


@dataclass
class BridgeMsti:
    id: str
    bridge: str
    disabled: bool
    identifier: int
    priority: str
    vlan_mapping: int
