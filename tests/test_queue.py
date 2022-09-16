from ros import QueueModule
from ros.queue import InterfaceQueue, SimpleQueue


class TestQueue:
    def test_queue(self, ros):
        assert isinstance(ros.queue, QueueModule)

    def test_queue_interface(self, ros):
        for i in ros.queue.interface:
            assert isinstance(i, InterfaceQueue)

    def test_queue_simple(self, ros):
        for i in ros.queue.simple:
            assert isinstance(i, SimpleQueue)
