from ros import PPPModule
from ros.ppp import PPPAAA


class TestPPP:
    def test_ppp(self, ros):
        assert isinstance(ros.ppp, PPPModule)

    def test_ppp_aaa(self, ros):
        assert isinstance(ros.ppp.aaa, PPPAAA)
