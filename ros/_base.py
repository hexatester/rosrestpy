from attr import define
from cattrs import unstructure
from typing import TYPE_CHECKING, Any, Dict, Generic, List, Type, TypeVar

if TYPE_CHECKING:
    from ros.ros import Ros

from ._utils import clean_before_put


@define
class BaseModule:
    ros: "Ros"
    filename: str = ""

    def __attrs_post_init__(self) -> None:
        if not self.filename:
            cname = self.__class__.__name__.lower()
            self.filename = "/" + cname.replace("module", "")

    @property
    def url(self) -> str:
        return self.filename


PR = TypeVar("PR", bound=object)


@define
class BaseProp(Generic[PR]):
    ros: "Ros"
    filename: str
    cl: Type[PR]

    def __call__(self, **kwds: Any) -> PR:
        return self.print(**kwds)

    def print(self, **kwds: Any) -> PR:
        o = self.ros.get_as(self.filename, self.cl, kwds)
        if hasattr(o, "_ros"):
            setattr(o, "_ros", self.ros)
        return o

    def set(self, **kwds: Any) -> PR:
        return self.ros.post_as(self.filename + "/set", None, kwds)


@define
class BaseProps(Generic[PR]):
    ros: "Ros"
    filename: str
    cl: Type[PR]
    _create: bool = True
    _disable: bool = True
    _delete: bool = True
    _write: bool = True

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
        return self.ros.put_as(self.filename, self.cl, data)

    def delete(self, o: PR):
        assert self._delete, "Not writeable"
        return self.remove(o)

    def _disabled(self, o: PR, s: bool) -> PR:
        assert self._write, "Not writeable"
        return self.ros.patch_as(
            self.filename + f"/{self._getid(o)}", self.cl, {"disabled": s}
        )

    def disable(self, o: PR) -> PR:
        assert self._disable, "Not allow disable"
        return self._disabled(o, True)

    def enable(self, o: PR) -> PR:
        return self._disabled(o, False)

    def print(self, **kwds: Any) -> List[PR]:
        return self.ros.get_as(self.filename, List[self.cl], kwds)

    def remove(self, o: PR):
        assert self._write, "Not writeable"
        self.ros.session.delete(self.filename + f"/{self._getid(o)}")

    def set(self, o: PR, nw: Dict[str, Any]):
        assert self._write, "Not writeable"
        return self.ros.patch_as(self.filename + f"/{self._getid(o)}", self.cl, nw)

    def unset(self):
        # assert self._write, "Not writeable"
        raise NotImplementedError("/unset function has not been implemented")
