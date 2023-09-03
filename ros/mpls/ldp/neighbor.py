from attr import dataclass


@dataclass
class LDPNeighbor:
    transport: str
    sending_targeted_hello: bool = None
    comment: str = None
    copy_from: str = None
    disabled: bool = None
    id: str = None
    addresses: str = None
    dynamic: bool = None
    inactive: bool = None
    local_transport: str = None
    on_demand: bool = None
    operational: bool = None
    passive: bool = None
    path_vector_limit: int = None
    peer: str = None
    used_afi: str = None
    vpls: bool = None
