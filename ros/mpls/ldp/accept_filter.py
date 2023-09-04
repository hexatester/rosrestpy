from attr import dataclass


@dataclass
class LDPAcceptFilter:
    vrf: str
    prefix: str
    neighbor: str = None
    accept: bool = None
    comment: str = None
    copy_from: str = None
    disabled: bool = None
    place_before: str = None
    id: str = None
    nextid: str = None
