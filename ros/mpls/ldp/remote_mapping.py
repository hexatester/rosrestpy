from attr import dataclass


@dataclass
class LDPRemoteMapping:
    label: str
    nexthop: str = None
    dst_address: str = None
    vrf: str = None
    comment: str = None
    disabled: bool = None
    copy_from: str = None
    id: str = None
    dynamic: bool = None
    inactive: bool = None
    path: str = None
    peer: str = None
