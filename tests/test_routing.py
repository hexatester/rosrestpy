from ros import RoutingModule
from ros.routing import RoutingTable


class TestRouting:
    def test_routing(self, ros):
        assert isinstance(ros.routing, RoutingModule)


class TestRoutingTable:
    def test_routing(self, ros):
        for i in ros.routing.table():
            assert isinstance(i, RoutingTable)
