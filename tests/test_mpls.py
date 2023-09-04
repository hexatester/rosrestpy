from ros import Ros, MPLSModule
from ros.mpls import MPLSLDP, MPLSInterface
from ros.mpls.ldp import (
    LDPInstance,
    LDPInterface,
    LDPLocalMapping,
    LDPNeighbor,
    LDPRemoteMapping,
)


class TestMPLS:
    def test_queue(self, ros: Ros):
        assert isinstance(ros.mpls, MPLSModule)


class TestLDP:
    def test_ldp(self, ros: Ros):
        assert isinstance(ros.mpls.ldp, MPLSLDP)

    def test_instance(self, ros: Ros):
        for i in ros.mpls.ldp():
            assert isinstance(i, LDPInstance)

    def test_interface(self, ros: Ros):
        for i in ros.mpls.ldp.interface():
            assert isinstance(i, LDPInterface)

    def test_local_mapping(self, ros: Ros):
        for i in ros.mpls.ldp.local_mapping():
            assert isinstance(i, LDPLocalMapping)

    def test_neighbor(self, ros: Ros):
        for i in ros.mpls.ldp.neighbor():
            assert isinstance(i, LDPNeighbor)

    def test_remote_mapping(self, ros: Ros):
        for i in ros.mpls.ldp.remote_mapping():
            assert isinstance(i, LDPRemoteMapping)


class TestInterface:
    def test_interface(self, ros: Ros):
        for i in ros.mpls.interface():
            assert isinstance(i, MPLSInterface)
