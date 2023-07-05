from ros._base import BaseProps
from .wireguard import Wireguard


class WireguardModule(BaseProps[Wireguard]):
    pass


__all__ = ["Wireguard", "WireguardModule"]
