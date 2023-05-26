from ros import Ros, ToolModule
from ros.tool import Netwatch


class TestTool:
    def test_tool(self, ros: Ros):
        assert isinstance(ros.tool, ToolModule)


class TestNetwatch:
    def test_netwatch(self, ros: Ros):
        for i in ros.tool.netwatch():
            assert isinstance(i, Netwatch)
