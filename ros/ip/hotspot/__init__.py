from ros._base import BaseProps
from .active import HotspotActive
from .cookie import HotspotCookie
from .host import HotspotHost
from .hotspot import HotspotServer
from .ip_binding import HotspotIPBinding
from .profile import HotspotProfile
from .service_port import HotspotServicePort
from .user import HotspotUserModule, HotspotUser
from .walled_garden import HotspotWalledGardenModule, HotspotWalledGarden


class HotspotModule(BaseProps[HotspotServer]):
    _active: BaseProps[HotspotActive] = None
    _cookie: BaseProps[HotspotCookie] = None
    _host: BaseProps[HotspotHost] = None
    _ip_binding: BaseProps[HotspotIPBinding] = None
    _user: HotspotUserModule = None
    _profile: BaseProps[HotspotProfile] = None
    _service_port: BaseProps[HotspotServicePort] = None
    _walled_garden: HotspotWalledGardenModule = None

    @property
    def active(self) -> BaseProps[HotspotActive]:
        if not self._active:
            self._active = BaseProps(self.ros, "/ip/hotspot/active", HotspotActive)
            self._active._create = False
            self._active._write = False
        return self._active

    @property
    def cookie(self) -> BaseProps[HotspotCookie]:
        if not self._cookie:
            self._cookie = BaseProps(self.ros, "/ip/hotspot/cookie", HotspotCookie)
            self._cookie._create = False
            self._cookie._write = False
        return self._cookie

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

    @property
    def service_port(self) -> BaseProps[HotspotServicePort]:
        if not self._service_port:
            self._service_port = BaseProps(
                self.ros, "/ip/hotspot/service-port", HotspotServicePort
            )
            self._service_port._delete = False
        return self._service_port

    @property
    def walled_garden(self) -> HotspotWalledGardenModule:
        if not self._walled_garden:
            self._walled_garden = HotspotWalledGardenModule(
                self.ros, "/ip/hotspot/walled-garden", HotspotWalledGarden
            )
        return self._walled_garden


__all__ = [
    "HotspotActive",
    "HotspotHost",
    "HotspotIPBinding",
    "HotspotProfile",
    "HotspotServer",
    "HotspotServicePort",
    "HotspotUser",
    "HotspotWalledGarden",
    "HotspotModule",
]
