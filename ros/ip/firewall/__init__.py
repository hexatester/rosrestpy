from typing import Optional

from ros._base import BaseSubModule

from .connection import IPFirewallConnectionModule
from .filter import IPFirewallFilterModule
from .layer7_protocol import IPFirewallLayer7ProtocolModule
from .mangle import IPFirewallMangleModule
from .nat import IPFirewallNatModule
from .raw import IPFirewallRawModule
from .service_port import IPFirewallServicePortModule


class IPFirewallModule(BaseSubModule):
    _connection: Optional[IPFirewallConnectionModule] = None
    _filter: Optional[IPFirewallFilterModule] = None
    _layer7_protocol: Optional[IPFirewallLayer7ProtocolModule] = None
    _mangle: Optional[IPFirewallMangleModule] = None
    _nat: Optional[IPFirewallNatModule] = None
    _raw: Optional[IPFirewallRawModule] = None
    _service_port: Optional[IPFirewallServicePortModule] = None

    @property
    def connection(self):
        if not self._connection:
            self._connection = IPFirewallConnectionModule(
                self.module, self.url + "/connection"
            )
        return self._connection

    @property
    def filter(self):
        if not self._filter:
            self._filter = IPFirewallFilterModule(self.module, self.url + "/filter")
        return self._filter

    @property
    def layer7_protocol(self):
        if not self._layer7_protocol:
            self._layer7_protocol = IPFirewallLayer7ProtocolModule(
                self.module, self.url + "/layer7-protocol"
            )
        return self._layer7_protocol

    @property
    def mangle(self):
        if not self._mangle:
            self._mangle = IPFirewallMangleModule(self.module, self.url + "/mangle")
        return self._mangle

    @property
    def nat(self):
        if not self._nat:
            self._nat = IPFirewallNatModule(self.module, self.url + "/nat")
        return self._nat

    @property
    def raw(self):
        if not self._raw:
            self._raw = IPFirewallRawModule(self.module, self.url + "/raw")
        return self._raw

    @property
    def service_port(self):
        if not self._service_port:
            self._service_port = IPFirewallServicePortModule(
                self.module, self.url + "/service-port"
            )
        return self._service_port
