from ros import InterfaceModule
from ros.inteface import BridgeModule, BridgePort


class TestInterface:
    def test_interface(self, ros):
        assert isinstance(ros.interface, InterfaceModule)


class TestBridge:
    def test_bridge(self, ros):
        assert isinstance(ros.bridge, BridgeModule)

    def test_bridge_port(self, ros):
        assert isinstance(ros.bridge.port, BridgePort)
