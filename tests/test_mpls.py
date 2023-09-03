from ros import Ros, MPLSModule
from ros.mpls import LDP, MPLSInterface


class TestMPLS:
    def test_queue(self, ros: Ros):
        assert isinstance(ros.mpls, MPLSModule)


class TestLDP:
    def test_ldp(self, ros: Ros):
        for i in ros.mpls.ldp():
            assert isinstance(i, LDP)


class TestInterface:
    def test_interface(self, ros: Ros):
        for i in ros.mpls.interface():
            assert isinstance(i, MPLSInterface)
