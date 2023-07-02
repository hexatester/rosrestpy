from ros._base import BaseProps
from .hotspot import HotspotServer


class HotspotModule(BaseProps[HotspotServer]):
    pass


__all__ = ["HotspotServer", "HotspotModule"]
