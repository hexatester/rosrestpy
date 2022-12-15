from attrs import define
from typing import List

from ros._base import BaseModule

from .aaa import PPPAAA
from .profile import PPPProfile
from .secret import PPPSecret


@define
class PPPModule(BaseModule):
    @property
    def aaa(self) -> PPPAAA:
        return self.ros.get_as(self.url + "/aaa", PPPAAA)

    def profile(self, **kwds) -> List[PPPProfile]:
        return self.ros.get_as(self.url + "/profile", List[PPPProfile], kwds)

    def secret(self, **kwds) -> List[PPPSecret]:
        return self.ros.get_as(self.url + "/secret", List[PPPSecret], kwds)


__all__ = ["PPPAAA", "PPPModule", "PPPProfile", "PPPSecret"]
