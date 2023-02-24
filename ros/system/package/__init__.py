from ros._base import BaseProps

from ._literals import UpdateChannel
from .package import Package
from .update import Update, UpdateModule


class PackageModule(BaseProps[Package]):
    _update: UpdateModule = None

    def downgrade(self):
        self.ros.post_as("/system/package/downgrade", None)

    @property
    def update(self) -> UpdateModule:
        if not self._update:
            self._update = UpdateModule(self.ros, "/system/package/update", Update)
        return self._update


__all__ = ["Package", "PackageModule", "Update", "UpdateChannel", "UpdateModule"]
