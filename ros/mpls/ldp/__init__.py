from ros._base import BaseProps

from .instance import LDPInstance
from .interface import LDPInterface
from .local_mapping import LDPLocalMapping
from .neighbor import LDPNeighbor
from .remote_mapping import LDPRemoteMapping


class MPLSLDP(BaseProps[LDPInstance]):
    _interface: BaseProps[LDPInterface] = None
    _neighbor: BaseProps[LDPNeighbor] = None
    _local_mapping: BaseProps[LDPLocalMapping] = None
    _remote_mapping: BaseProps[LDPLocalMapping] = None

    @property
    def interface(self):
        if not self._interface:
            self._interface = BaseProps(self.ros, "/mpls/ldp/interface", LDPInterface)
        return self._interface

    @property
    def local_mapping(self):
        if not self._local_mapping:
            self._local_mapping = BaseProps(
                self.ros, "/mpls/ldp/local-mapping", LDPLocalMapping
            )
        return self._local_mapping

    @property
    def neighbor(self):
        if not self._neighbor:
            self._neighbor = BaseProps(self.ros, "/mpls/ldp/neighbor", LDPNeighbor)
        return self._neighbor

    @property
    def remote_mapping(self):
        if not self._remote_mapping:
            self._remote_mapping = BaseProps(
                self.ros, "/mpls/ldp/remote-mapping", LDPRemoteMapping
            )
        return self._remote_mapping
