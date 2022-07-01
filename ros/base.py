from attr import define
from typing import TYPE_CHECKING, Type, TypeVar

if TYPE_CHECKING:
    from ros.ros import Ros


@define
class BaseModule:
    ros: "Ros"
    url: str = ""

    def __attrs_post_init__(self) -> None:
        if self.url:
            self.url = "/" + self.url
        else:
            self.url = "/" + self.__class__.__name__.lower()


BM = TypeVar("BM", bound=BaseModule)


@define
class BaseSubModule:
    module: BM
    url: str = ""

    def __attrs_post_init__(self) -> None:
        if self.url:
            self.url = self.module.url + "/" + self.url
        else:
            self.url = self.module.url + "/" + self.__class__.__name__.lower()
