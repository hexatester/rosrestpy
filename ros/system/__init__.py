from typing import List

from ros.base import BaseModule

from .health import Health
from .history import History
from .identity import Identity
from .license import License
from .note import Note
from .resource import Resource
from .routerboard import RouterBOARD


class System(BaseModule):
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
