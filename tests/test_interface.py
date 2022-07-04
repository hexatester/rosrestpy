from ros import InterfaceModule
from ros.inteface import BridgeModule, Bridge, BridgeMsti, BridgePort, BridgeVlan


class TestInterface:
    def test_interface(self, ros):
        assert isinstance(ros.interface, InterfaceModule)


class TestBridge:
    def test_bridge(self, ros):
        assert isinstance(ros.bridge, BridgeModule)

    def test_bridge_bridge(self, ros):
        for item in ros.bridge.print():
            assert isinstance(item, Bridge)

    def test_bridge_msti(self, ros):
        for item in ros.bridge.msti:
            assert isinstance(item, BridgeMsti)

    def test_bridge_port(self, ros):
        for item in ros.bridge.port:
            assert isinstance(item, BridgePort)

    def test_bridge_vlan(self, ros):
        for item in ros.bridge.vlan:
            assert isinstance(item, BridgeVlan)
