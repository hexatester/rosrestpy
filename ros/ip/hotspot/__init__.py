from ros._base import BaseProps
from .active import HotspotActive
from .hotspot import HotspotServer
from .profile import HotspotProfile
from .user import HotspotUserModule, HotspotUser


class HotspotModule(BaseProps[HotspotServer]):
    _active: BaseProps[HotspotActive] = None
    _user: HotspotUserModule = None
    _profile: BaseProps[HotspotProfile] = None

    @property
    def active(self) -> BaseProps[HotspotActive]:
        if not self._active:
            self._active = BaseProps(self.ros, "/ip/hotspot/active", HotspotActive)
            self._active._create = False
            self._active._write = False
        return self._active

    @property
    def user(self) -> HotspotUserModule:
        if not self._user:
            self._user = HotspotUserModule(self.ros, "/ip/hotspot/user", HotspotUser)
        return self._user

    @property
    def profile(self) -> BaseProps[HotspotProfile]:
        if not self._profile:
            self._profile = BaseProps(self.ros, "/ip/hotspot/profile", HotspotProfile)
        return self._profile


__all__ = [
    "HotspotActive",
    "HotspotProfile",
    "HotspotServer",
    "HotspotUser",
    "HotspotModule",
]
