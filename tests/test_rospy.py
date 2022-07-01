from ros import __version__, Log


class TestRos:
    def test_version(self):
        assert __version__ == "0.1.3"

    def test_log(self, ros):
        for log in ros.log:
            assert isinstance(log, Log)
