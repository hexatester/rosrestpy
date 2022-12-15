from typing import Any, List

from ros._base import BaseModule

from .health import Health
from .history import History
from .identity import Identity
from .license import License
from .logging import Logging
from .note import Note
from .package import Package, PackageModule
from .resource import Resource
from .routerboard import RouterBOARD


class SystemModule(BaseModule):
    _package: Package = None

    def health(self, **kwds: Any) -> List[Health]:
        return self.ros.get_as(self.url + "/health", List[Health], kwds)

    def history(self, **kwds: Any) -> List[History]:
        return self.ros.get_as(self.url + "/history", List[History], kwds)

    @property
    def identity(self) -> Identity:
        return self.ros.get_as(self.url + "/identity", Identity)

    @property
    def license(self) -> License:
        return self.ros.get_as(self.url + "/license", License)

    def logging(self, **kwds: Any) -> List[Logging]:
        return self.ros.get_as(self.url + "/logging", List[Logging], kwds)

    @property
    def note(self) -> Note:
        return self.ros.get_as(self.url + "/note", Note)

    @property
    def package(self) -> PackageModule:
        if not self._package:
            self._package = PackageModule(self, "/package")
        return self._package

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
    "Logging",
    "Note",
    "Resource",
    "RouterBOARD",
    "SystemModule",
]
