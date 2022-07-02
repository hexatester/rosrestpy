from ros import InterfaceModule


class TestInterface:
    def test_interface(self, ros):
        assert isinstance(ros.interface, InterfaceModule)
