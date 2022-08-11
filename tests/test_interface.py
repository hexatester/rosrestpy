from ros import InterfaceModule
from ros.inteface.bridge import BridgeModule, Bridge, BridgeMsti, BridgePort, BridgeVlan
from ros.inteface.ethernet import EthernetModule, EthernetList
from ros.inteface.list import InterfaceListModule, InterfaceList, InterfaceListMember


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


class TestEthernet:
    def test_ethernet(self, ros):
        assert isinstance(ros.interface.ethernet, EthernetModule)

    def test_ethernet_list(self, ros):
        for item in ros.interface.ethernet.print():
            assert isinstance(item, EthernetList)


class TestList:
    def test_list(self, ros):
        assert isinstance(ros.interface.list, InterfaceListModule)

    def test_list_list(self, ros):
        for item in ros.interface.list.print():
            assert isinstance(item, InterfaceList)

    def test_list_member(self, ros):
        for item in ros.interface.list.member:
            assert isinstance(item, InterfaceListMember)
