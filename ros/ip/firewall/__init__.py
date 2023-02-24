from attr import define

from ros._base import BaseModule, BaseProps

from .connection import IPConnection
from .filter import IPFirewallFilter
from .nat import IPFirewallNAT


@define
class IPFirewallModule:
    ros: BaseModule
    filename: str
    _connection: BaseProps[IPConnection] = None
    _filter: BaseProps[IPFirewallFilter] = None
    _nat: BaseProps[IPFirewallNAT] = None

    @property
    def connection(self) -> BaseProps[IPConnection]:
        if not self._connection:
            self._connection = BaseProps(
                self.ros, "/ip/firewall/connection", IPConnection
            )
        return self._connection

    @property
    def filter(self) -> BaseProps[IPFirewallFilter]:
        if not self._filter:
            self._filter = BaseProps(self.ros, "/ip/firewall/filter", IPFirewallFilter)
        return self._filter

    @property
    def nat(self) -> BaseProps[IPFirewallNAT]:
        if not self._nat:
            self._nat = BaseProps(self.ros, "/ip/firewall/nat", IPFirewallNAT)
        return self._nat
