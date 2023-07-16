from attr import dataclass


@dataclass
class BFDConfiguration:
    forbid_bfd: bool
    interfaces: str = None
    addresses: str = None
    address_list: str = None
    min_rx: float = None
    min_tx: float = None
    multiplier: int = None
    comment: str = None
    disabled: bool = False
    vrf: str = None
    id: str = None
    nextid: str = None
    inactive: bool = None
    copy_from: str = None
    place_before: str = None
