import json
from attr import define
from requests import Session
from requests.auth import HTTPBasicAuth
from typing import Any, List, Optional, Type, TypeVar

from . import InterfaceModule, IPModule, SystemModule, ToolModule

from . import Error, Log

from .inteface import BridgeModule
from ._utils import clean_data, make_converter

_converter = make_converter()

T = TypeVar("T", bound=object)


@define
class Ros:
    server: str
    username: str
    password: str
    session: Session = Session()
    secure: bool = False
    filename: str = "rest"
    url: str = ""
    _interface: Optional[InterfaceModule] = None
    _ip: Optional[IPModule] = None
    _system: Optional[SystemModule] = None
    _tool: Optional[ToolModule] = None

    def __attrs_post_init__(self) -> None:
        if not self.server.endswith("/"):
            self.server += "/"
        self.session.auth = HTTPBasicAuth(self.username, self.password)
        self.password = ""
        self.url = self.server + self.filename

    def get_as(self, filename: str, cl: Type[T]) -> T:
        res = self.session.get(self.url + filename, verify=self.secure)
        odata = json.loads(res.text)
        data: Any = clean_data(odata)
        if data and "error" in data:
            raise _converter.structure(data, Error)
        return _converter.structure(data, cl)

    def post_as(
        self,
        filename: str,
        cl: Type[T],
        json_: Any = None,
        data: Any = None,
    ) -> T:
        res = self.session.post(
            self.url + filename,
            data=data,
            json=json_,
            verify=self.secure,
        )
        odata = json.loads(res.text)
        data = clean_data(odata)
        if data and "error" in data:
            raise _converter.structure(data, Error)
        return _converter.structure(data, cl)

    @property
    def bridge(self) -> BridgeModule:
        return self.interface.bridge

    @property
    def interface(self):
        if not self._interface:
            self._interface = InterfaceModule(self)
        return self._interface

    @property
    def ip(self):
        if not self._ip:
            self._ip = IPModule(self)
        return self._ip

    @property
    def system(self):
        if not self._system:
            self._system = SystemModule(self)
        return self._system

    @property
    def tool(self):
        if not self._tool:
            self._tool = ToolModule(self, "/tool")
        return self._tool

    @property
    def log(self):
        return self.get_as("/log", List[Log])

    def ping(self, address: str, count: int = 4):
        return self.tool.ping(address, count)
