from ros import Interface


class TestInterface:
    def test_interface(self, ros):
        assert isinstance(ros.interface, Interface)
