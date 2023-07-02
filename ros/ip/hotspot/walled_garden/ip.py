from attr import dataclass
from typing import Literal

ActionLiteral = Literal["accept", "drop", "reject"]


@dataclass
class HotspotWalledGardenIP:
    action: ActionLiteral = "accept"
    server: str = None
    src_address: str = None
    dst_address: str = None
    src_address_list: str = None
    dst_address_list: str = None
    protocol: str = None
    dst_port: str = None
    dst_host: str = None
    comment: str = None
    disabled: bool = False
    id: str = None
    copy_from: str = None
    invalid: bool = False
    place_before: str = None
