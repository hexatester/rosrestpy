from ros._base import BaseProps
from .user import HotspotUser


class HotspotUserModule(BaseProps[HotspotUser]):
    pass


__all__ = ["HotspotUser", "HotspotUserModule"]
