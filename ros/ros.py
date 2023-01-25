try:
    import ujson as json
except ImportError:
    import json  # type: ignore[no-redef]
from attr import define
from requests import Session
from requests.auth import HTTPBasicAuth
from typing import Any, Dict, List, Optional, Type, TypeVar

from . import (
    InterfaceModule,
    IPModule,
    PPPModule,
    QueueModule,
    RoutingModule,
    SystemModule,
    ToolModule,
)

from . import Error, Log

from .inteface import BridgeModule
from ._utils import clean_data, clean_filters, make_converter

_converter = make_converter()

T = TypeVar("T", bound=object)


@define
class BaseRos:
    server: str
    username: str
    password: str
    session: Session = Session()
    secure: bool = False
    filename: str = "rest"
    url: str = ""

    def __attrs_post_init__(self) -> None:
        if not self.server.endswith("/"):
            self.server += "/"
        self.session.auth = HTTPBasicAuth(self.username, self.password)
        self.session.verify = self.secure
        self.password = ""
        self.url = self.server + self.filename

    def get_as(self, filename: str, cl: Type[T], filters: Dict[str, Any] = None) -> T:
        res = self.session.get(
            self.url + filename,
            params=clean_filters(filters),
            verify=self.secure,
        )
        odata = json.loads(res.text)
        data: Any = clean_data(odata)
        if data and "error" in data:
            raise _converter.structure(data, Error)
        try:
            return _converter.structure(data, cl)
        except Exception as e:
            raise e

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
        )
        odata = json.loads(res.text)
        data = clean_data(odata)
        if data and "error" in data:
            raise _converter.structure(data, Error)
        return _converter.structure(data, cl)

    def patch_as(
        self,
        filename: str,
        cl: Type[T],
        json_: Any = None,
        data: Any = None,
    ) -> T:
        res = self.session.patch(
            self.url + filename,
            data=data,
            json=json_,
        )
        odata = json.loads(res.text)
        data = clean_data(odata)
        if data and "error" in data:
            raise _converter.structure(data, Error)
        return _converter.structure(data, cl)

    def put_as(
        self,
        filename: str,
        cl: Type[T],
        json_: Any = None,
        data: Any = None,
    ) -> T:
        res = self.session.put(
            self.url + filename,
            data=data,
            json=json_,
        )
        odata = json.loads(res.text)
        data = clean_data(odata)
        if data and "error" in data:
            raise _converter.structure(data, Error)
        return _converter.structure(data, cl)


class Ros(BaseRos):
    _interface: Optional[InterfaceModule] = None
    _ip: Optional[IPModule] = None
    _ppp: Optional[PPPModule] = None
    _queue: Optional[QueueModule] = None
    _routing: Optional[RoutingModule] = None
    _system: Optional[SystemModule] = None
    _tool: Optional[ToolModule] = None
    """
    Ros class that represent a routeros device.

    Attributes
    ----------
    :param str server: The device's Rest API url, example https://192.168.88.1/
    :param str username: Username
    :param str password: Password
    :param requests.Session session: A requests.Session instance
    :param bool secure: Valdiate ssl cert
    :param str filename: Base filename of the rest API, default to `rest`
    :param str url: The device's Rest API url with base filename, default to https://server/rest
    """

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
    def ppp(self):
        if not self._ppp:
            self._ppp = PPPModule(self)
        return self._ppp

    @property
    def queue(self):
        if not self._queue:
            self._queue = QueueModule(self)
        return self._queue

    @property
    def routing(self):
        if not self._routing:
            self._routing = RoutingModule(self)
        return self._routing

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

    def log(self, **kwds: Any):
        return self.get_as("/log", List[Log], kwds)

    def ping(self, address: str, count: int = 4):
        return self.tool.ping(address, count)
