import cattr
import json
from attr import define
from requests import Session
from requests.auth import HTTPBasicAuth
from typing import Any, Dict, List, Optional, Type, TypeVar

from . import System

from . import Log

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
            data = self.clean_key(odata)
        elif isinstance(odata, list):
            data = list()
            for val in odata:
                if isinstance(val, dict):
                    data.append(self.clean_key(val))
                else:
                    data.append(val)
        return cattr.structure(data, cl)

    @staticmethod
    def clean_key(d: Dict[str, Any]) -> dict:
        nd = dict()
        for k, v in d.items():
            k = k.replace("-", "_")
            if k == ".id":
                k = "id"
            nd[k] = v
        return nd

    @property
    def system(self):
        if not self._system:
            self._system = System(self)
        return self._system

    @property
    def log(self):
        return self.get_as("/log", List[Log])
