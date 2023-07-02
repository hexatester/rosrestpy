from ros._base import BaseProps
from .active import HotspotActive
from .host import HotspotHost
from .hotspot import HotspotServer
from .ip_binding import HotspotIPBinding
from .profile import HotspotProfile
from .user import HotspotUserModule, HotspotUser


class HotspotModule(BaseProps[HotspotServer]):
    _active: BaseProps[HotspotActive] = None
    _host: BaseProps[HotspotHost] = None
    _ip_binding: BaseProps[HotspotIPBinding] = None
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
    def host(self) -> BaseProps[HotspotHost]:
        if not self._host:
            self._host = BaseProps(self.ros, "/ip/hotspot/host", HotspotHost)
            self._host._create = False
            self._host._write = False
        return self._host

    @property
    def ip_binding(self) -> BaseProps[HotspotIPBinding]:
        if not self._ip_binding:
            self._ip_binding = BaseProps(
                self.ros, "/ip/hotspot/ip-binding", HotspotIPBinding
            )
        return self._ip_binding

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
    "HotspotHost",
    "HotspotProfile",
    "HotspotServer",
    "HotspotUser",
    "HotspotModule",
]
