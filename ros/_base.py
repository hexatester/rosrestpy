from attr import define, asdict
from cattrs import unstructure
from typing import TYPE_CHECKING, Any, Dict, Generic, List, Type, TypeVar, Union

if TYPE_CHECKING:
    from ros.ros import Ros

from ._utils import clean_before_put


@define
class BaseModule:
    ros: "Ros"
    url: str = ""

    def __attrs_post_init__(self) -> None:
        if not self.url:
            cname = self.__class__.__name__.lower()
            self.url = "/" + cname.replace("module", "")


BM = TypeVar("BM", bound=BaseModule)


PR = TypeVar("PR", bound=object)


@define
class BaseProp(Generic[PR]):
    ros: "Ros"
    url: str
    cl: Type[PR]

    def __call__(self, **kwds: Any) -> PR:
        return self.print(**kwds)

    def print(self, **kwds: Any) -> PR:
        return self.ros.get_as(self.url, self.cl, kwds)

    def set(self, **kwds: Any) -> PR:
        return self.ros.post_as(self.url + "/set", None, kwds)


@define
class BaseProps(Generic[PR]):
    mod: BaseModule
    url: str
    cl: Type[PR]
    _create: bool = True
    _delete: bool = True
    _write: bool = True

    @property
    def ros(self):
        return self.mod.ros

    @property
    def filename(self):
        return self.url

    def __attrs_post_init__(self) -> None:
        if not self.url.startswith(self.mod.url):
            self.url = self.mod.url.rstrip("/") + self.url

    def __call__(self, **kwds: Any) -> List[PR]:
        return self.print(**kwds)

    @staticmethod
    def _getid(o: PR):
        assert hasattr(o, "id")
        return getattr(o, "id")

    def add(self, o: PR) -> PR:
        assert self._write and self._create, "Not writeable"
        data = unstructure(o)
        data = clean_before_put(data)
        return self.mod.ros.put_as(self.url, self.cl, data)

    def delete(self, o: PR):
        assert self._write and self._delete, "Not writeable"
        return self.remove(o)

    def _disabled(self, o: PR, s: bool) -> PR:
        assert self._write, "Not writeable"
        return self.mod.ros.patch_as(
            self.url + f"/{self._getid(o)}", self.cl, {"disabled": s}
        )

    def disable(self, o: PR) -> PR:
        return self._disabled(o, True)

    def enable(self, o: PR) -> PR:
        return self._disabled(o, False)

    def print(self, **kwds: Any) -> List[PR]:
        return self.mod.ros.get_as(self.url, List[self.cl], kwds)

    def remove(self, o: PR):
        assert self._write, "Not writeable"
        self.mod.ros.session.delete(self.url + f"/{self._getid(o)}")

    def set(self, o: PR, nw: Dict[str, Any]):
        assert self._write, "Not writeable"
        return self.mod.ros.patch_as(self.url + f"/{self._getid(o)}", self.cl, nw)

    def unset(self):
        # assert self._write, "Not writeable"
        raise NotImplementedError("/unset function has not been implemented")
