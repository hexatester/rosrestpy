from attr import define
from typing import TYPE_CHECKING, Any, Generic, List, Type, TypeVar, Union

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
            if not self.url.startswith(self.module.url):
                self.url = self.module.url + self.url
        else:
            cname = self.__class__.__name__.lower()
            self.url = self.module.url + "/" + cname.replace("module", "")


PR = TypeVar("PR", bound=object)


@define
class BaseProp(Generic[PR]):
    mod: Union[BaseModule, BaseSubModule]
    url: str
    cl: Type[PR]

    def __call__(self, **kwds: Any) -> PR:
        return self.print(**kwds)

    def print(self, **kwds: Any) -> PR:
        return self.mod.ros.get_as(self.url, self.cl, kwds)


@define
class BaseProps(Generic[PR]):
    mod: Union[BaseModule, BaseSubModule]
    url: str
    cl: Type[PR]

    def __call__(self, **kwds: Any) -> List[PR]:
        return self.print(**kwds)

    def print(self, **kwds: Any) -> List[PR]:
        return self.mod.ros.get_as(self.url, List[self.cl], kwds)
