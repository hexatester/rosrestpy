from ros import Ros, RoutingModule
from ros.routing import RoutingRule, RoutingTable


class TestRouting:
    def test_routing(self, ros: Ros):
        assert isinstance(ros.routing, RoutingModule)


class TestRoutingRule:
    def test_routing(self, ros: Ros):
        for i in ros.routing.rule():
            assert isinstance(i, RoutingRule)


class TestRoutingTable:
    def test_routing(self, ros: Ros):
        for i in ros.routing.table():
            assert isinstance(i, RoutingTable)
