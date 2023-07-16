from ros import Ros, RoutingModule
from ros.routing import RoutingId, Nexthop, RoutingRule, RoutingTable
from ros.routing.bfd import BFDConfiguration, BFDSession, BFDModule


class TestRouting:
    def test_routing(self, ros: Ros):
        assert isinstance(ros.routing, RoutingModule)


class TestBFD:
    def test_bfd(self, ros: Ros):
        assert isinstance(ros.routing.bfd, BFDModule)

    def test_configuration(self, ros: Ros):
        for i in ros.routing.bfd.configuration():
            assert isinstance(i, BFDConfiguration)

    def test_session(self, ros: Ros):
        for i in ros.routing.bfd.session():
            assert isinstance(i, BFDSession)


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
