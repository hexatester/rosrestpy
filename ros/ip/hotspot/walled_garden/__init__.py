from attr import dataclass
from typing import Literal

from ros._base import BaseProps
from .ip import HotspotWalledGardenIP

ActionLiteral = Literal["allow", "deny"]


@dataclass
class HotspotWalledGarden:
    action: ActionLiteral
    server: str = None
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


class HotspotWalledGardenModule(BaseProps[HotspotWalledGarden]):
    _ip: BaseProps[HotspotWalledGardenIP] = None

    @property
    def ip(self) -> BaseProps[HotspotWalledGardenIP]:
        if not self._ip:
            self._ip = BaseProps(
                self.ros, "/ip/hotspot/walled-garden/ip", HotspotWalledGardenIP
            )
        return self._ip


__all__ = ["HotspotWalledGarden", "HotspotWalledGarden", "HotspotWalledGardenIP"]
