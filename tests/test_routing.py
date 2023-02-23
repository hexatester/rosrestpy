from ros import Ros, RoutingModule
from ros.routing import RoutingTable


class TestRouting:
    def test_routing(self, ros: Ros):
        assert isinstance(ros.routing, RoutingModule)


class TestRoutingTable:
    def test_routing(self, ros: Ros):
        for i in ros.routing.table():
            assert isinstance(i, RoutingTable)
