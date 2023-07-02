from attr import dataclass
from typing import Union

from ros._base import BaseProps
from .profile import HotspotUserProfile


@dataclass
class HotspotUser:
    name: str
    password: str = None
    server: str = "all"
    address: str = None
    mac_address: str = None
    profile: str = "default"
    routes: str = None
    email: str = None
    limit_uptime: str = None
    limit_bytes_in: Union[str, int] = None
    limit_bytes_out: Union[str, int] = None
    limit_bytes_total: Union[str, int] = None
    disabled: bool = False
    comment: str = None
    copy_from: str = None
    id: str = None
    dynamic: bool = None
    bytes_in: int = None
    bytes_out: int = None
    packets_in: int = None
    packets_out: int = None
    uptime: str = None

    def __str__(self):
        return self.name


class HotspotUserModule(BaseProps[HotspotUser]):
    _profile: BaseProps[HotspotUserProfile] = None

    @property
    def profile(self) -> BaseProps[HotspotUserProfile]:
        if not self._profile:
            self._profile = BaseProps(
                self.ros, "/ip/hotspot/user/profile", HotspotUserProfile
            )
        return self._profile


__all__ = ["HotspotUser", "HotspotUserProfile", "HotspotUserModule"]
