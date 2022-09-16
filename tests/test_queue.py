from ros import QueueModule
from ros.queue import SimpleQueue


class TestQueue:
    def test_queue(self, ros):
        assert isinstance(ros.queue, QueueModule)

    def test_queue_simple(self, ros):
        for i in ros.queue.simple:
            assert isinstance(i, SimpleQueue)
