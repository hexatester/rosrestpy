import json
from attr import define
from requests import Session
from requests.auth import HTTPBasicAuth
from typing import Any, List, Optional, Type, TypeVar

from . import InterfaceModule
from . import IPModule
from . import SystemModule

from . import Log

from .inteface import BridgeModule
from ._utils import clean_key, make_converter

T = TypeVar("T", bound=object)
_converter = make_converter()


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

    def __attrs_post_init__(self) -> None:
        if not self.server.endswith("/"):
            self.server += "/"
        self.session.auth = HTTPBasicAuth(self.username, self.password)
        self.password = ""
        self.url = self.server + self.filename

    def get_as(self, filename: str, cl: Type[T]) -> T:
        res = self.session.get(self.url + filename, verify=self.secure)
        odata = json.loads(res.text)
        data: Any = None
        if isinstance(odata, dict):
            data = clean_key(odata)
        elif isinstance(odata, list):
            data = list()
            for val in odata:
                if isinstance(val, dict):
                    data.append(clean_key(val))
                else:
                    data.append(val)
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
    def log(self):
        return self.get_as("/log", List[Log])
