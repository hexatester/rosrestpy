from ros import Ros, QueueModule
from ros.queue import InterfaceQueue, SimpleQueue, QueueTree, QueueType


class TestQueue:
    def test_queue(self, ros: Ros):
        assert isinstance(ros.queue, QueueModule)

    def test_queue_interface(self, ros: Ros):
        for i in ros.queue.interface():
            assert isinstance(i, InterfaceQueue)

    def test_queue_simple(self, ros: Ros):
        for i in ros.queue.simple():
            assert isinstance(i, SimpleQueue)

    def test_queue_tree(self, ros: Ros):
        for i in ros.queue.tree():
            assert isinstance(i, QueueTree)

    def test_queue_type(self, ros: Ros):
        for i in ros.queue.type():
            assert isinstance(i, QueueType)
