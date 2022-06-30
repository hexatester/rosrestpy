import json
from attr import define
from requests import Session
from requests.auth import HTTPBasicAuth
from typing import Any, List, Optional, Type, TypeVar

from . import Interface
from . import IP
from . import System

from . import Log

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
    _interface: Optional[Interface] = None
    _ip: Optional[IP] = None
    _system: Optional[System] = None

    def __attrs_post_init__(self) -> None:
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
    def interface(self):
        if not self._interface:
            self._interface = Interface(self)
        return self._interface

    @property
    def ip(self):
        if not self._ip:
            self._ip = IP(self)
        return self._ip

    @property
    def system(self):
        if not self._system:
            self._system = System(self)
        return self._system

    @property
    def log(self):
        return self.get_as("/log", List[Log])
