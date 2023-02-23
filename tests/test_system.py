from ros import Ros, SystemModule
from ros.system import Health, History, Identity, License, Note, Resource, RouterBOARD
from ros.system.package import PackageModule, Package, Update


class TestSystem:
    def test_system(self, ros: Ros):
        assert isinstance(ros.system, SystemModule)

    def test_health(self, ros: Ros):
        for health in ros.system.health():
            assert isinstance(health, Health)

    def test_history(self, ros: Ros):
        for history in ros.system.history():
            assert isinstance(history, History)

    def test_identity(self, ros: Ros):
        assert isinstance(ros.system.identity, Identity)

    def test_license(self, ros: Ros):
        assert isinstance(ros.system.license, License)

    def test_note(self, ros: Ros):
        assert isinstance(ros.system.note, Note)

    def test_resource(self, ros: Ros):
        assert isinstance(ros.system.resource, Resource)

    def test_routerboard(self, ros: Ros):
        assert isinstance(ros.system.routerboard, RouterBOARD)


class TestPackage:
    def test_package(self, ros: Ros):
        assert isinstance(ros.system.package, PackageModule)

    def test_package_print(self, ros: Ros):
        for i in ros.system.package():
            assert isinstance(i, Package)


class TestPackageUpdate:
    def test_print(self, ros: Ros):
        assert isinstance(ros.system.package.update.print(), Update)

    def test_cancel(self, ros: Ros):
        assert ros.system.package.update.cancel() is None

    def test_check_for_updates(self, ros: Ros):
        for i in ros.system.package.update.check_for_updates():
            assert isinstance(i, Update)

    def test_set(self, ros: Ros):
        old_update: Update = ros.system.package.update.print()
        if old_update.channel == "stable":
            ros.system.package.update.set(channel="testing")
            new_update: Update = ros.system.package.update.print()
            assert new_update.channel == "testing"
        else:
            ros.system.package.update.set(channel="stable")
            new_update: Update = ros.system.package.update.print()
            assert new_update.channel == "stable"
        ros.system.package.update.set(channel=old_update.channel)
