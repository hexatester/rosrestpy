from ros import Ros, InterfaceModule
from ros.inteface.bridge import BridgeModule, Bridge, BridgeMsti, BridgePort, BridgeVlan
from ros.inteface.eoip import EoIP
from ros.inteface.ethernet import InterfaceEthernet
from ros.inteface.list import InterfaceListModule, InterfaceList, InterfaceListMember


class TestInterface:
    def test_module(self, ros: Ros):
        assert isinstance(ros.interface, InterfaceModule)


class TestBridge:
    def test_module(self, ros: Ros):
        assert isinstance(ros.bridge, BridgeModule)

    def test_bridge(self, ros: Ros):
        for item in ros.bridge():
            assert isinstance(item, Bridge)

    def test_msti(self, ros: Ros):
        for item in ros.bridge.msti():
            assert isinstance(item, BridgeMsti)

    def test_port(self, ros: Ros):
        for item in ros.bridge.port():
            assert isinstance(item, BridgePort)

    def test_vlan(self, ros: Ros):
        for item in ros.bridge.vlan():
            assert isinstance(item, BridgeVlan)


class TestEoIP:
    def test_eoip(self, ros: Ros):
        for item in ros.interface.eoip():
            assert isinstance(item, EoIP)


class TestEthernet:
    def test_ethernet(self, ros: Ros):
        assert ros.interface.ethernet.cl == InterfaceEthernet

    def test_list(self, ros: Ros):
        for item in ros.interface.ethernet():
            assert isinstance(item, InterfaceEthernet)


class TestList:
    def test_module(self, ros: Ros):
        assert isinstance(ros.interface.list, InterfaceListModule)

    def test_list(self, ros: Ros):
        for item in ros.interface.list.print():
            assert isinstance(item, InterfaceList)

    def test_member(self, ros: Ros):
        for item in ros.interface.list.member():
            assert isinstance(item, InterfaceListMember)
