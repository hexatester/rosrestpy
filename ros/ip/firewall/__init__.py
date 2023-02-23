from attr import define
from typing import Optional

from ros._base import BaseModule, BaseProps

from .connection import IPConnection


@define
class IPFirewallModule:
    mod: BaseModule
    url: str
    _connection: Optional[BaseProps[IPConnection]] = None

    @property
    def connection(self) -> BaseProps[IPConnection]:
        if not self._connection:
            self._connection = BaseProps(
                self.mod.ros, self.url + "/connection", IPConnection
            )
        return self._connection
