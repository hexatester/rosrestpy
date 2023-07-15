from ros import Ros, RoutingModule
from ros.routing import RoutingId, Nexthop, RoutingRule, RoutingTable


class TestRouting:
    def test_routing(self, ros: Ros):
        assert isinstance(ros.routing, RoutingModule)


class TestRoutingId:
    def test_routing_id(self, ros: Ros):
        for i in ros.routing.id():
            assert isinstance(i, RoutingId)


class TestNexthop:
    def test_nexthop(self, ros: Ros):
        for i in ros.routing.nexthop():
            assert isinstance(i, Nexthop)


class TestRoutingRule:
    def test_rule(self, ros: Ros):
        for i in ros.routing.rule():
            assert isinstance(i, RoutingRule)


class TestRoutingTable:
    def test_table(self, ros: Ros):
        for i in ros.routing.table():
            assert isinstance(i, RoutingTable)
