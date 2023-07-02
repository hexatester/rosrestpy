from ros._base import BaseProps
from .hotspot import HotspotServer
from .profile import HotspotProfile


class HotspotModule(BaseProps[HotspotServer]):
    _profile: BaseProps[HotspotProfile] = None

    @property
    def profile(self) -> BaseProps[HotspotProfile]:
        if not self._profile:
            self._profile = BaseProps(self.ros, "/ip/hotspot/profile", HotspotProfile)
        return self._profile


__all__ = ["HotspotProfile", "HotspotServer", "HotspotModule"]
