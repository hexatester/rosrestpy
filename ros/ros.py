try:
    import ujson as json
except ImportError:
    import json  # type: ignore[no-redef]
from attr import define
from requests import Session
from requests.exceptions import ConnectionError, HTTPError
from requests.auth import HTTPBasicAuth
from typing import Any, Dict, List, Type, TypeVar

import logging

from . import (
    SysLogger,
    InterfaceModule,
    IPModule,
    MPLSModule,
    PPPModule,
    QueueModule,
    RoutingModule,
    SystemModule,
    ToolModule,
    UserModule,
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
    secure: object = False
    filename: str = "rest"
    url: str = ""
    # Logger Instance
    _loglevel: int = logging.INFO
    _logger: SysLogger = SysLogger(__name__, _loglevel)

    def __attrs_post_init__(self) -> None:
        if not self.server.endswith("/"):
            self.server += "/"
        # Authentication to the REST API is performed via HTTP Basic Auth.
        self.session.auth = HTTPBasicAuth(self.username, self.password)
        self.session.verify = self.secure
        # self.password = ""
        self.url = self.server + self.filename
        self.logger.new_session()

    @property
    def logger(self):
        return self._logger

    @property
    def loglevel(self):
        return self.logger.loglevel

    @loglevel.setter
    def loglevel(self, loglevel: int):
        self._loglevel = loglevel
        self.logger.syslogger.setLevel(loglevel)

    def log_request(self, url: str, filename: str):
        self.logger.log_message(f'API Call: {url + filename}', logging.INFO)

    def log_httpstatus(self, response: object = None):
        if response.request:
            self.logger.log_message(f'HTTP Request: {response.request}', logging.DEBUG)
        if response:
            self.logger.log_message(f'HTTP Status: {response.status_code}', logging.DEBUG)

        response.raise_for_status()

    def log_apistatus(self, data: object) -> Any:
        """
        API errors could be considered soft
        """
        if data and "error" in data:
            status = _converter.structure(data, Error)
            self.logger.log_message(status, logging.WARN)
            return status

        return False

    def get_as(self, filename: str, cl: Type[T], filters: Dict[str, Any] = None) -> T:
        """To get the records.

        Args:
            filename (str): Path
            cl (Type[T]): Class
            filters (Dict[str, Any], optional): Query for specific obj. Defaults to None.

        Raises:
            _converter.structure: Error parser
            e: Exception

        Returns:
            T: Object of cl
        """
        odata: Any = None
        data: Any = []
        try:
            self.log_request(self.url, filename)
            res = self.session.get(
                self.url + filename,
                params=clean_filters(filters),
                verify=self.secure,
            )

            odata = res.json()
            data = clean_data(odata)
            if self.log_apistatus(data):
                return

            self.log_httpstatus(res)

        except (ConnectionError, HTTPError) as e:
            self.logger.log_message(e, logging.ERROR)
            return
        except Exception as e:
            self.logger.log_message(e, logging.CRITICAL)
            raise e

        return _converter.structure(data, cl)

    def delete_as(self, filename: str, json_: Any = None, data: Any = None) -> bool:
        """To delete the records.

        Args:
            filename (str): Path
            json_ (Any, optional): data to be sent in json format. Defaults to None.
            data (Any, optional): data to be sent in form format. Defaults to None.

        Raises:
            _converter.structure: Error parser
            e: Exception

        Returns:
            None
        """
        odata: Any = None
        data: Any = []
        try:
            self.log_request(self.url, filename)
            res = self.session.delete(self.url + filename)

            if res.text:
                odata = res.json()
                data = clean_data(odata)

            if self.log_apistatus(data):
                return False

            self.log_httpstatus(res)

        except (ConnectionError, HTTPError) as e:
            self.logger.log_message(e, logging.ERROR)
            return False
        except Exception as e:
            self.logger.log_message(e, logging.CRITICAL)
            raise e

        return True

    def post_as(self, filename: str,  cl: Type[T], json_: Any = None, data: Any = None) -> T:
        """Universal method to get access to all console commands.

        Args:
            filename (str): Path
            cl (Type[T]): Class of the should be returned object
            json_ (Any, optional): data to be sent in json format. Defaults to None.
            data (Any, optional): data to be sent in form format. Defaults to None.

        Raises:
            _converter.structure: Error parser

        Returns:
            T: Object of cl
        """
        odata: str = None
        data: Any = []
        try:
            self.log_request(self.url, filename)
            res = self.session.post(
                self.url + filename,
                data=data,
                json=json_,
            )
            odata = res.json()
            data = clean_data(odata)
            if self.log_apistatus(data):
                return

            self.log_httpstatus(res)

        except (ConnectionError, HTTPError) as e:
            self.logger.log_message(e, logging.ERROR)
            return
        except Exception as e:
            self.logger.log_message(e, logging.CRITICAL)
            raise e

        return _converter.structure(data, cl)

    def patch_as(self, filename: str, cl: Type[T], json_: Any = None, data: Any = None) -> T:
        """To update a single record.

        Args:
            filename (str): Path
            cl (Type[T]): Class of object that should be returned
            json_ (Any, optional): data to be sent in json format. Defaults to None.
            data (Any, optional): data to be sent in form format. Defaults to None.

        Raises:
            _converter.structure: Error parser

        Returns:
            T: Object of cl
        """
        odata: str = None
        data: Any = []
        try:
            self.log_request(self.url, filename)
            res = self.session.patch(
                self.url + filename,
                data=data,
                json=json_,
            )

            odata = res.json()
            data = clean_data(odata)
            if self.log_apistatus(data):
                return

            self.log_httpstatus(res)

        except (ConnectionError, HTTPError) as e:
            self.logger.log_message(e, logging.ERROR)
            return
        except Exception as e:
            self.logger.log_message(e, logging.CRITICAL)
            raise e

        return _converter.structure(data, cl)

    def put_as(self, filename: str, cl: Type[T], json_: Any = None, data: Any = None) -> T:
        """To create a new record.

        Args:
            filename (str): Path
            cl (Type[T]): Class of object that should be returned
            json_ (Any, optional): data to be sent in json format. Defaults to None.
            data (Any, optional): data to be sent in form format. Defaults to None.

        Raises:
            _converter.structure: Error parser

        Returns:
            T: Object of cl
        """
        odata: str = None
        data: Any = []
        try:
            self.log_request(self.url, filename)
            res = self.session.put(
                self.url + filename,
                data=data,
                json=json_,
            )

            odata = res.json()
            data = clean_data(odata)
            if self.log_apistatus(data):
                return

            self.log_httpstatus(res)

        except (ConnectionError, HTTPError) as e:
            self.logger.log_message(e, logging.ERROR)
            return
        except Exception as e:
            self.logger.log_message(e, logging.CRITICAL)
            raise e

        return _converter.structure(data, cl)


class Ros(BaseRos):
    _interface: InterfaceModule = None
    _ip: IPModule = None
    _mpls: MPLSModule = None
    _ppp: PPPModule = None
    _queue: QueueModule = None
    _routing: RoutingModule = None
    _system: SystemModule = None
    _tool: ToolModule = None
    _user: UserModule = None
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
        """/interface/bridge"""
        return self.interface.bridge

    @property
    def wireguard(self):
        """/interface/wireguard"""
        return self.interface.wireguard

    @property
    def interface(self):
        """/interface"""
        if not self._interface:
            self._interface = InterfaceModule(self)
        return self._interface

    @property
    def ip(self):
        """/ip"""
        if not self._ip:
            self._ip = IPModule(self)
        return self._ip

    @property
    def mpls(self):
        """/mpls"""
        if not self._mpls:
            self._mpls = MPLSModule(self)
        return self._mpls

    @property
    def ppp(self):
        """/ppp"""
        if not self._ppp:
            self._ppp = PPPModule(self)
        return self._ppp

    @property
    def queue(self):
        """/queue"""
        if not self._queue:
            self._queue = QueueModule(self)
        return self._queue

    @property
    def routing(self):
        """/routing"""
        if not self._routing:
            self._routing = RoutingModule(self)
        return self._routing

    @property
    def system(self):
        """/system"""
        if not self._system:
            self._system = SystemModule(self)
        return self._system

    @property
    def tool(self):
        """/tool"""
        if not self._tool:
            self._tool = ToolModule(self, "/tool")
        return self._tool

    @property
    def user(self):
        """/user"""
        if not self._user:
            self._user = UserModule(self, "/user")
        return self._user

    def log(self, **kwds: Any):
        """Get logs"""
        return self.get_as("/log", List[Log], kwds)

    def ping(self, address: str, count: int = 4):
        return self.tool.ping(address, count)
