from attr import define
from typing import Optional

from ros._base import BaseModule, BaseProps

from .connection import IPConnection


@define
class IPFirewallModule:
    ros: BaseModule
    filename: str
    _connection: Optional[BaseProps[IPConnection]] = None

    @property
    def connection(self) -> BaseProps[IPConnection]:
        if not self._connection:
            self._connection = BaseProps(
                self.ros, "/ip/firewall/connection", IPConnection
            )
        return self._connection
