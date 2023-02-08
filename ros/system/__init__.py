from ros._base import BaseModule, BaseProps

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
    _health: BaseProps[Health] = None
    _history: BaseProps[History] = None
    _logging: BaseProps[Logging] = None
    _package: Package = None

    @property
    def health(self):
        if not self._health:
            self._health = BaseProps(self, self.url + "/health", Health)
        return self._health

    @property
    def history(self):
        if not self._history:
            self._history = BaseProps(self, self.url + "/history", History)
        return self._history

    @property
    def identity(self) -> Identity:
        return self.ros.get_as(self.url + "/identity", Identity)

    @property
    def license(self) -> License:
        return self.ros.get_as(self.url + "/license", License)

    @property
    def logging(self):
        if not self._logging:
            self._logging = BaseProps(self, self.url + "/logging", Logging)
        return self._logging

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
