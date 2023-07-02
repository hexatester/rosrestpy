from attr import dataclass
from typing import Literal

ActionLiteral = Literal["allow", "deny"]


@dataclass
class HotspotWalledGarden:
    action: ActionLiteral
    server: str
    src_address: str = None
    method: str = None
    dst_host: str = None
    dst_port: str = None
    path: str = None
    comment: str = None
    disabled: bool = False
    hits: int = None
    id: str = None
    copy_from: str = None
    place_before: str = None
    dst_address: str = None
