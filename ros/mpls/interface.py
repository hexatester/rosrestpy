from attr import dataclass


@dataclass
class MPLSInterface:
    interface: str
    mpls_mtu: int = None
    input: bool = None
    comment: str = None
    copy_from: str = None
    disabled: bool = None
    place_before: str = None
    id: str = None
