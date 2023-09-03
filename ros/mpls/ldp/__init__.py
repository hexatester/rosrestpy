from ros._base import BaseProps

from .instance import LDPInstance
from .interface import LDPInterface


class MPLSLDP(BaseProps[LDPInstance]):
    _interface: BaseProps[LDPInterface] = None

    @property
    def interface(self):
        if not self._interface:
            self._interface = BaseProps(self.ros, "/mpls/ldp/interface", LDPInterface)
        return self._interface
