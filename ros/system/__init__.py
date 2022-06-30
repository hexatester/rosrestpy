from attr import define
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from ros.ros import Ros

from .health import Health
from .history import History
from .identity import Identity
from .license import License
from .note import Note
from .resource import Resource
from .routerboard import RouterBOARD


@define
class System:
    ros: "Ros"
    url: str = ""

    def __attrs_post_init__(self) -> None:
        self.url = "/" + self.__class__.__name__.lower()

    @property
    def health(self) -> List[Health]:
        return self.ros.get_as(self.url + "/health", List[Health])

    @property
    def history(self) -> List[History]:
        return self.ros.get_as(self.url + "/history", List[History])

    @property
    def identity(self) -> Identity:
        return self.ros.get_as(self.url + "/identity", Identity)

    @property
    def license(self) -> License:
        return self.ros.get_as(self.url + "/license", License)

    @property
    def note(self) -> Note:
        return self.ros.get_as(self.url + "/note", Note)

    @property
    def resource(self) -> Resource:
        return self.ros.get_as(self.url + "/resource", Resource)

    @property
    def routerboard(self) -> RouterBOARD:
        return self.ros.get_as(self.url + "/routerboard", RouterBOARD)


__all__ = [
    "Health",
    "History",
    "Identity",
    "License",
    "Note",
    "Resource",
    "RouterBOARD",
    "System",
]
