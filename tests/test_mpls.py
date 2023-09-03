from ros import Ros, MPLSModule
from ros.mpls import MPLSLDP, MPLSInterface
from ros.mpls.ldp import LDPInstance


class TestMPLS:
    def test_queue(self, ros: Ros):
        assert isinstance(ros.mpls, MPLSModule)


class TestLDP:
    def test_ldp(self, ros: Ros):
        assert isinstance(ros.mpls.ldp, MPLSLDP)

    def test_instance(self, ros: Ros):
        for i in ros.mpls.ldp():
            assert isinstance(i, LDPInstance)


class TestInterface:
    def test_interface(self, ros: Ros):
        for i in ros.mpls.interface():
            assert isinstance(i, MPLSInterface)
