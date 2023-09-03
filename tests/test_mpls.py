from ros import Ros, MPLSModule
from ros.mpls import LDP


class TestMPLS:
    def test_queue(self, ros: Ros):
        assert isinstance(ros.mpls, MPLSModule)


class TestLDP:
    def test_ldp(self, ros: Ros):
        for i in ros.mpls.ldp():
            assert isinstance(i, LDP)
