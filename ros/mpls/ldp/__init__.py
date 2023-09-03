from ros._base import BaseProps

from .instance import LDPInstance
from .interface import LDPInterface
from .neighbor import LDPNeighbor


class MPLSLDP(BaseProps[LDPInstance]):
    _interface: BaseProps[LDPInterface] = None
    _neighbor: BaseProps[LDPNeighbor] = None

    @property
    def interface(self):
        if not self._interface:
            self._interface = BaseProps(self.ros, "/mpls/ldp/interface", LDPInterface)
        return self._interface

    @property
    def neighbor(self):
        if not self._neighbor:
            self._neighbor = BaseProps(self.ros, "/mpls/ldp/neighbor", LDPNeighbor)
        return self._neighbor
