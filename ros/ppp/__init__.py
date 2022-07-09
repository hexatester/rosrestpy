from attrs import define
from typing import List

from ros._base import BaseModule

from .aaa import PPPAAA
from .profile import PPPProfile


@define
class PPPModule(BaseModule):
    @property
    def aaa(self) -> PPPAAA:
        return self.ros.get_as(self.url + "/aaa", PPPAAA)

    @property
    def profile(self) -> List[PPPProfile]:
        return self.ros.get_as(self.url + "/profile", List[PPPProfile])


__all__ = ["PPPAAA", "PPPModule", "PPPProfile"]
