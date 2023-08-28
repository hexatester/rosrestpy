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
from .script import Script, ScriptModule


class SystemModule(BaseModule):
    _health: BaseProps[Health] = None
    _history: BaseProps[History] = None
    _logging: BaseProps[Logging] = None
    _package: PackageModule = None
    _script: ScriptModule = None

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
            self._history._delete = False
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
            self._logging._create = False
        return self._logging

    @property
    def note(self) -> Note:
        return self.ros.get_as("/system/note", Note)

    @property
    def package(self) -> PackageModule:
        if not self._package:
            self._package = PackageModule(self.ros, "/system/package", Package)
            self._package._create = False
            self._package._write = False
        return self._package

    @property
    def resource(self) -> Resource:
        return self.ros.get_as("/system/resource", Resource)

    @property
    def routerboard(self) -> RouterBOARD:
        return self.ros.get_as("/system/routerboard", RouterBOARD)

    @property
    def script(self) -> ScriptModule:
        if not self._script:
            self._script = ScriptModule(self.ros, "/system/script", Script)
        return self._script

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
    "Script",
    "RouterBOARD",
    "SystemModule",
]
