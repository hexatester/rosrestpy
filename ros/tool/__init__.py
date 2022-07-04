import json
from typing import List

from ros import _converter
from ros.error import Error
from ros._base import BaseModule
from ros._utils import clean_data

from .ping import Ping


class ToolModule(BaseModule):
    def ping(self, address: str, count: int = 4):
        data = {"address": address, "count": count}
        res = self.ros.session.post(self.url + "/ping", json=data, verify=self.secure)
        odata = json.loads(res.text)
        data = clean_data(odata)
        if data and "error" in data:
            raise _converter.structure(data, Error)
        return _converter.structure(data, List[Ping])
