from ros import Ros, InterfaceModule
from ros.inteface.bridge import BridgeModule, Bridge, BridgeMsti, BridgePort, BridgeVlan
from ros.inteface.ethernet import InterfaceEthernet
from ros.inteface.list import InterfaceListModule, InterfaceList, InterfaceListMember

from ros._base import BaseProps


class TestInterface:
    def test_interface(self, ros: Ros):
        assert isinstance(ros.interface, InterfaceModule)


class TestBridge:
    def test_bridge(self, ros: Ros):
        assert isinstance(ros.bridge, BridgeModule)

    def test_bridge_bridge(self, ros: Ros):
        for item in ros.bridge():
            assert isinstance(item, Bridge)

    def test_bridge_msti(self, ros: Ros):
        for item in ros.bridge.msti:
            assert isinstance(item, BridgeMsti)

    def test_bridge_port(self, ros: Ros):
        for item in ros.bridge.port:
            assert isinstance(item, BridgePort)

    def test_bridge_vlan(self, ros: Ros):
        for item in ros.bridge.vlan:
            assert isinstance(item, BridgeVlan)


class TestEthernet:
    def test_ethernet(self, ros: Ros):
        assert ros.interface.ethernet.cl == InterfaceEthernet

    def test_ethernet_list(self, ros: Ros):
        for item in ros.interface.ethernet():
            assert isinstance(item, InterfaceEthernet)


class TestList:
    def test_list(self, ros: Ros):
        assert isinstance(ros.interface.list, InterfaceListModule)

    def test_list_list(self, ros: Ros):
        for item in ros.interface.list.print():
            assert isinstance(item, InterfaceList)

    def test_list_member(self, ros: Ros):
        for item in ros.interface.list.member():
            assert isinstance(item, InterfaceListMember)
