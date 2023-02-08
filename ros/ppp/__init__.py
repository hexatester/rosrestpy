from typing import List

from ros._base import BaseModule, BaseProps

from .aaa import PPPAAA
from .profile import PPPProfile
from .secret import PPPSecret


class PPPModule(BaseModule):
    _profile: BaseProps[PPPProfile] = None
    _secret: BaseProps[PPPSecret] = None

    @property
    def aaa(self) -> PPPAAA:
        return self.ros.get_as(self.url + "/aaa", PPPAAA)

    @property
    def profile(self):
        if not self._profile:
            self._profile = BaseProps(self, self.url + "/profile", PPPProfile)
        return self._profile

    @property
    def secret(self):
        if not self._secret:
            self._secret = BaseProps(self, self.url + "/secret", PPPSecret)
        return self._secret


__all__ = ["PPPAAA", "PPPModule", "PPPProfile", "PPPSecret"]
