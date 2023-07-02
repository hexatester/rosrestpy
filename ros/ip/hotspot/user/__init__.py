from ros._base import BaseProps
from .user import HotspotUser
from .profile import HotspotUserProfile


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
