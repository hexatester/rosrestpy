from ros import System
from ros.system import Health, History, Identity, License, Note, Resource, RouterBOARD
from typing import List


class TestSystem:
    def test_system(self, ros):
        assert isinstance(ros.system, System)

    def test_health(self, ros):
        for health in ros.system.health:
            assert isinstance(health, Health)

    def test_history(self, ros):
        for history in ros.system.history:
            assert isinstance(history, History)

    def test_identity(self, ros):
        assert isinstance(ros.system.identity, Identity)

    def test_license(self, ros):
        assert isinstance(ros.system.license, License)

    def test_note(self, ros):
        assert isinstance(ros.system.note, Note)

    def test_resource(self, ros):
        assert isinstance(ros.system.resource, Resource)

    def test_routerboard(self, ros):
        assert isinstance(ros.system.routerboard, RouterBOARD)
