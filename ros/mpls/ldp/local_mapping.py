from attr import dataclass


@dataclass
class LDPLocalMapping:
    vrf: str = None
    dst_address: str = None
    label: str = None
    comment: str = None
    copy_from: str = None
    disabled: bool = None
    dynamic: bool = None
    egress: bool = None
    gateway: bool = None
    id: str = None
    adv_path: str = None
    peers: str = None
    pw_fec: str = None
    vpls: bool = None
