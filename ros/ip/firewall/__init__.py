from attr import define

from ros._base import BaseModule, BaseProps

from .address_list import IPAddressList
from .connection import IPConnection
from .filter import IPFirewallFilter
from .mangle import IPFirewallMangle
from .nat import IPFirewallNAT


@define
class IPFirewallModule:
    ros: BaseModule
    filename: str
    _address_list: BaseProps[IPAddressList] = None
    _connection: BaseProps[IPConnection] = None
    _filter: BaseProps[IPFirewallFilter] = None
    _mangle: BaseProps[IPFirewallMangle] = None
    _nat: BaseProps[IPFirewallNAT] = None

    @property
    def address_list(self) -> BaseProps[IPAddressList]:
        if not self._address_list:
            self._address_list = BaseProps(
                self.ros, "/ip/firewall/address-list", IPAddressList
            )
        return self._address_list

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
    def mangle(self) -> BaseProps[IPFirewallMangle]:
        if not self._mangle:
            self._mangle = BaseProps(self.ros, "/ip/firewall/mangle", IPFirewallMangle)
        return self._mangle

    @property
    def nat(self) -> BaseProps[IPFirewallNAT]:
        if not self._nat:
            self._nat = BaseProps(self.ros, "/ip/firewall/nat", IPFirewallNAT)
        return self._nat


__all__ = [
    "IPConnection",
    "IPFirewallFilter",
    "IPFirewallMangle",
    "IPFirewallNAT",
    "IPFirewallModule",
]
