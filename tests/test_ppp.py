from ros import PPPModule
from ros.ppp import PPPAAA, PPPProfile


class TestPPP:
    def test_ppp(self, ros):
        assert isinstance(ros.ppp, PPPModule)

    def test_aaa(self, ros):
        assert isinstance(ros.ppp.aaa, PPPAAA)

    def test_profile(self, ros):
        for i in ros.ppp.profile:
            assert isinstance(i, PPPProfile)
