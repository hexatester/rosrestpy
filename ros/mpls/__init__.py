from ros._base import BaseModule, BaseProps

from .forwarding_table import MPLSForwardingTable
from .interface import MPLSInterface
from .ldp import MPLSLDP, LDPInstance


class MPLSModule(BaseModule):
    _forwarding_table: BaseProps[MPLSForwardingTable] = None
    _interface: BaseProps[MPLSInterface] = None
    _ldp: MPLSLDP = None

    @property
    def forwarding_table(self):
        if not self._forwarding_table:
            self._forwarding_table = BaseProps(
                self.ros, "/mpls/forwarding-table", MPLSForwardingTable
            )
            self._forwarding_table._create = False
            self._forwarding_table._delete = False
            self._forwarding_table._write = False
        return self._forwarding_table

    @property
    def interface(self):
        if not self._interface:
            self._interface = BaseProps(self.ros, "/mpls/interface", MPLSInterface)
        return self._interface

    @property
    def ldp(self):
        if not self._ldp:
            self._ldp = MPLSLDP(self.ros, "/mpls/ldp", LDPInstance)
        return self._ldp
