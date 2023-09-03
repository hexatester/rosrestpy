from ros._base import BaseModule, BaseProps

from .interface import MPLSInterface
from .ldp import LDP


class MPLSModule(BaseModule):
    _interface: BaseProps[MPLSInterface] = None
    _ldp: BaseProps[LDP] = None

    @property
    def interface(self):
        if not self._interface:
            self._interface = BaseProps(self.ros, "/mpls/interface", MPLSInterface)
        return self._interface

    @property
    def ldp(self):
        if not self._ldp:
            self._ldp = BaseProps(self.ros, "/mpls/ldp", LDP)
        return self._ldp
