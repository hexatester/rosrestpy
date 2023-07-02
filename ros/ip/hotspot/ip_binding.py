from attr import dataclass
from typing import Literal

TypeLiteral = Literal["blocked", "bypassed", "regular"]


@dataclass
class HotspotIPBinding:
    mac_address: str = None
    address: str = None
    to_address: str = None
    server: str = "all"
    type: TypeLiteral = "regular"
    comment: str = None
    disabled: bool = False
    place_before: str = None
    copy_from: str = None
    id: str = None
    bypassed: bool = False
    blocked: bool = False

    def __attrs_post_init__(self) -> None:
        if not self.mac_address and not self.address:
            raise ValueError("failure: address or mac-address is required")
