from typing import List, Optional

from ros._base import BaseModule

from .bridge import BridgeModule, Bridge
from .interface import Interface


class InterfaceModule(BaseModule):
    _brigde: Optional[BridgeModule] = None

    @property
    def bridge(self) -> BridgeModule:
        if not self._brigde:
            self._brigde = BridgeModule(self, "/bridge")
        return self._brigde

    def print(self) -> List[Interface]:
        return self.ros.get_as(self.url, List[Interface])


__all__ = ["BridgeModule", "Bridge", "InterfaceModule", "Interface"]
