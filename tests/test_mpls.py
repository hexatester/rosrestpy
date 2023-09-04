from ros import Ros, MPLSModule
from ros.mpls import MPLSForwardingTable, MPLSLDP, MPLSInterface
from ros.mpls.ldp import (
    LDPAcceptFilter,
    LDPAdvertiseFilter,
    LDPInstance,
    LDPInterface,
    LDPLocalMapping,
    LDPNeighbor,
    LDPRemoteMapping,
)


class TestForwardingTable:
    def test_forwarding_table(self, ros: Ros):
        for i in ros.mpls.forwarding_table():
            assert isinstance(i, MPLSForwardingTable)


class TestMPLS:
    def test_queue(self, ros: Ros):
        assert isinstance(ros.mpls, MPLSModule)


class TestLDP:
    def test_ldp(self, ros: Ros):
        assert isinstance(ros.mpls.ldp, MPLSLDP)

    def test_instance(self, ros: Ros):
        for i in ros.mpls.ldp():
            assert isinstance(i, LDPInstance)

    def test_accept_filter(self, ros: Ros):
        for i in ros.mpls.ldp.accept_filter():
            assert isinstance(i, LDPAcceptFilter)

    def test_advertise_filter(self, ros: Ros):
        for i in ros.mpls.ldp.advertise_filter():
            assert isinstance(i, LDPAdvertiseFilter)

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
