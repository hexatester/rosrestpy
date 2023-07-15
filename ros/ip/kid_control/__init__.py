from ros._base import BaseProps
from .device import Device
from .kid import KidControl


class KidControlModule(BaseProps[KidControl]):
    _device: BaseProps[Device] = None

    @property
    def device(self) -> BaseProps[Device]:
        if not self._device:
            self._device = BaseProps(self.ros, "/ip/kid-control/device", Device)
        return self._device


__all__ = ["Device", "KidControl", "KidControlModule"]
