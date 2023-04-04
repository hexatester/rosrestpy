from ros._base import BaseModule, BaseProps

from .interface import InterfaceQueue
from .simple import SimpleQueue
from .tree import QueueTree


class QueueModule(BaseModule):
    _interface: BaseProps[InterfaceQueue] = None
    _simple: BaseProps[SimpleQueue] = None
    _tree: BaseProps[QueueTree] = None

    @property
    def interface(self):
        if not self._interface:
            self._interface = BaseProps(self.ros, "/queue/interface", InterfaceQueue)
        return self._interface

    @property
    def simple(self):
        if not self._simple:
            self._simple = BaseProps(self.ros, "/queue/simple", SimpleQueue)
        return self._simple

    @property
    def tree(self):
        if not self._tree:
            self._tree = BaseProps(self.ros, "/queue/tree", QueueTree)
        return self._tree
