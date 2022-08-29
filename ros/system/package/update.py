from attr import dataclass
from typing import List, Optional

from ros._base import BaseSubModule
from . import UpdateChannel


@dataclass
class Update:
    channel: UpdateChannel
    installed_version: str
    latest_version: Optional[str] = None
    status: Optional[str] = None
    section: Optional[int] = None


class UpdateModule(BaseSubModule):
    def print(self) -> Update:
        return self.module.ros.get_as(self.url, Update)

    def cancel(self):
        self.module.ros.post_as(self.url + "/cancel", None)

    def check_for_updates(self) -> Update:
        return self.module.ros.post_as(self.url + "/check-for-updates", List[Update])

    def download(self):
        self.module.ros.post_as(self.url + "/download", None)

    def install(self):
        self.module.ros.post_as(self.url + "/install", None)

    def set(self, channel: UpdateChannel):
        data = {"channel": channel}
        return self.module.ros.post_as(self.url + "/set", None, data)
