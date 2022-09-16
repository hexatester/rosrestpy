from attr import define
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from ros.ros import Ros


@define
class BaseModule:
    ros: "Ros"
    url: str = ""

    def __attrs_post_init__(self) -> None:
        if not self.url:
            cname = self.__class__.__name__.lower()
            self.url = "/" + cname.replace("module", "")


BM = TypeVar("BM", bound=BaseModule)


@define
class BaseSubModule:
    module: BM
    url: str = ""
    _ros: "Ros" = None

    @property
    def ros(self) -> "Ros":
        if not self._ros:
            self._ros = self.module.ros
        return self._ros

    def __attrs_post_init__(self) -> None:
        if self.url:
            self.url = self.module.url + self.url
        else:
            cname = self.__class__.__name__.lower()
            self.url = self.module.url + "/" + cname.replace("module", "")
