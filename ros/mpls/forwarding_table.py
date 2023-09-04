from attr import dataclass


@dataclass
class MPLSForwardingTable:
    id: str
    label: str
    type: str
    ldp: bool = False
    vpls: bool = False
    vrf: str = None
    nexthops: str = None
    prefix: str = None
