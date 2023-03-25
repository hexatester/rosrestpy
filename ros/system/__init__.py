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
    _package: PackageModule = None

    @property
    def health(self):
        if not self._health:
            self._health = BaseProps(self.ros, "/system/health", Health)
            self._health._write = False
        return self._health

    @property
    def history(self):
        if not self._history:
            self._history = BaseProps(self.ros, "/system/history", History)
            self._history._write = False
        return self._history

    @property
    def identity(self) -> Identity:
        return self.ros.get_as("/system/identity", Identity)

    @property
    def license(self) -> License:
        return self.ros.get_as("/system/license", License)

    @property
    def logging(self):
        if not self._logging:
            self._logging = BaseProps(self.ros, "/system/logging", Logging)
            self._logging._write = False
        return self._logging

    @property
    def note(self) -> Note:
        return self.ros.get_as("/system/note", Note)

    @property
    def package(self) -> PackageModule:
        if not self._package:
            self._package = PackageModule(self.ros, "/system/package", Package)
        return self._package

    @property
    def resource(self) -> Resource:
        return self.ros.get_as("/system/resource", Resource)

    @property
    def routerboard(self) -> RouterBOARD:
        return self.ros.get_as("/system/routerboard", RouterBOARD)

    def ssh_exec(
        self,
        address: str,
        command: str,
        output_to_file: str = None,
        port: int = None,
        src_address: str = None,
        user: str = None,
        vrf: str = None,
    ) -> str:
        data = {"address": address, "command": command}
        return self.ros.post_as("/system/ssh-exec", str, data)


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
