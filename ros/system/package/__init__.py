from typing import List
from ros._base import BaseSubModule

from ._literals import UpdateChannel
from .package import Package
from .update import Update, UpdateModule


class PackageModule(BaseSubModule):
    _update: UpdateModule = None

    def downgrade(self):
        self.module.ros.post_as(self.url + "/downgrade", None)

    def __call__(self, **kwds) -> List[Package]:
        return self.print(**kwds)

    def print(self, **kwds) -> List[Package]:
        return self.module.ros.get_as(self.url, List[Package], kwds)

    @property
    def update(self) -> UpdateModule:
        if not self._update:
            self._update = UpdateModule(self.module, "/package/update")
        return self._update


__all__ = ["Package", "PackageModule", "Update", "UpdateChannel", "UpdateModule"]
