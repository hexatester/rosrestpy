from ros import Ros, PPPModule
from ros.ppp import PPPAAA, PPPProfile, PPPSecret


class TestPPP:
    def test_ppp(self, ros: Ros):
        assert isinstance(ros.ppp, PPPModule)

    def test_aaa(self, ros: Ros):
        assert isinstance(ros.ppp.aaa, PPPAAA)

    def test_profile(self, ros: Ros):
        for i in ros.ppp.profile():
            assert isinstance(i, PPPProfile)

    def test_secret(self, ros: Ros):
        for i in ros.ppp.secret():
            assert isinstance(i, PPPSecret)
