from ros import __version__


class TestRos:
    def test_version(self):
        assert __version__ == "0.1.1"
