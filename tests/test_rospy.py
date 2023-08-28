from ros import __version__, Log, Ros


class TestRos:
    def test_version(self):
        assert __version__ == "0.10.0"

    def test_log(self, ros: Ros):
        for log in ros.log():
            assert isinstance(log, Log)
