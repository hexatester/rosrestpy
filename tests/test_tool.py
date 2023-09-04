from ros import Ros, ToolModule
from ros.tool.netwatch import Netwatch
from ros.tool.profile import Profile


class TestTool:
    def test_tool(self, ros: Ros):
        assert isinstance(ros.tool, ToolModule)


class TestNetwatch:
    def test_netwatch(self, ros: Ros):
        for i in ros.tool.netwatch():
            assert isinstance(i, Netwatch)


class TestProfile:
    def test_profile(self, ros: Ros):
        for i in ros.tool.profile():
            assert isinstance(i, Profile)
