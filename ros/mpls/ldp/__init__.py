from ros._base import BaseProps

from .accept_filter import LDPAcceptFilter
from .advertise_filter import LDPAdvertiseFilter
from .instance import LDPInstance
from .interface import LDPInterface
from .local_mapping import LDPLocalMapping
from .neighbor import LDPNeighbor
from .remote_mapping import LDPRemoteMapping


class MPLSLDP(BaseProps[LDPInstance]):
    _accept_filter: BaseProps[LDPAcceptFilter] = None
    _advertise_filter: BaseProps[LDPAdvertiseFilter] = None
    _interface: BaseProps[LDPInterface] = None
    _neighbor: BaseProps[LDPNeighbor] = None
    _local_mapping: BaseProps[LDPLocalMapping] = None
    _remote_mapping: BaseProps[LDPLocalMapping] = None

    @property
    def accept_filter(self):
        if not self._accept_filter:
            self._accept_filter = BaseProps(
                self.ros, "/mpls/ldp/accept-filter", LDPAcceptFilter
            )
        return self._accept_filter

    @property
    def advertise_filter(self):
        if not self._advertise_filter:
            self._advertise_filter = BaseProps(
                self.ros, "/mpls/ldp/advertise-filter", LDPAdvertiseFilter
            )
        return self._advertise_filter

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
