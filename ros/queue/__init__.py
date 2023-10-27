from ros._base import BaseModule, BaseProps

from .interface import InterfaceQueue
from .simple import SimpleQueue, SimpleQueueModule
from .tree import QueueTree, QueueTreeModule
from .type import QueueType


class QueueModule(BaseModule):
    _interface: BaseProps[InterfaceQueue] = None
    _simple: SimpleQueueModule = None
    _tree: QueueTreeModule = None
    _type: BaseProps[QueueType] = None

    @property
    def interface(self):
        if not self._interface:
            self._interface = BaseProps(self.ros, "/queue/interface", InterfaceQueue)
        return self._interface

    @property
    def simple(self):
        if not self._simple:
            self._simple = SimpleQueueModule(self.ros, "/queue/simple", SimpleQueue)
        return self._simple

    @property
    def tree(self):
        if not self._tree:
            self._tree = QueueTreeModule(self.ros, "/queue/tree", QueueTree)
        return self._tree

    @property
    def type(self):
        if not self._type:
            self._type = BaseProps(self.ros, "/queue/type", QueueType)
        return self._type
