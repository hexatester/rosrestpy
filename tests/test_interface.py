from ros import InterfaceModule
from ros.inteface import BridgeModule, BridgePort, BridgeVlan


class TestInterface:
    def test_interface(self, ros):
        assert isinstance(ros.interface, InterfaceModule)


class TestBridge:
    def test_bridge(self, ros):
        assert isinstance(ros.bridge, BridgeModule)

    def test_bridge_port(self, ros):
        for item in ros.bridge.port:
            assert isinstance(item, BridgePort)

    def test_bridge_vlan(self, ros):
        for item in ros.bridge.vlan:
            assert isinstance(item, BridgeVlan)
