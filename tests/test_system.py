from ros import System


class TestSystem:
    def test_system(self, ros):
        assert isinstance(ros.system, System)
