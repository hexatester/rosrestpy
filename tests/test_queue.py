from ros import QueueModule


class TestQueue:
    def test_queue(self, ros):
        assert isinstance(ros.queue, QueueModule)
