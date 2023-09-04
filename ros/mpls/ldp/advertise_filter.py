from attr import dataclass


@dataclass
class LDPAdvertiseFilter:
    vrf: str
    prefix: str
    neighbor: str = None
    advertise: bool = None
    comment: str = None
    copy_from: str = None
    disabled: bool = None
    place_before: str = None
    id: str = None
    nextid: str = None
