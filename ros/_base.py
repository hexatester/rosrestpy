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
            self.url = "/" + cname.strip("module")


BM = TypeVar("BM", bound=BaseModule)


@define
class BaseSubModule:
    module: BM
    url: str = ""

    def __attrs_post_init__(self) -> None:
        if self.url:
            self.url = self.module.url + self.url
        else:
            cname = self.__class__.__name__.lower()
            self.url = self.module.url + "/" + cname.strip("module")
