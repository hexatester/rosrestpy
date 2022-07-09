from attrs import define

from ros._base import BaseModule

from .aaa import PPPAAA


@define
class PPPModule(BaseModule):
    @property
    def aaa(self) -> PPPAAA:
        return self.ros.get_as(self.url + "/aaa", PPPAAA)


__all__ = ["PPPAAA", "PPPModule"]
