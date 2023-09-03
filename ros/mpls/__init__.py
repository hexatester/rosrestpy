from ros._base import BaseModule, BaseProps

from .interface import MPLSInterface
from .ldp import MPLSLDP, LDPInstance


class MPLSModule(BaseModule):
    _interface: BaseProps[MPLSInterface] = None
    _ldp: MPLSLDP = None

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
