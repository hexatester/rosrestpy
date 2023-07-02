from attr import dataclass
from typing import Union


@dataclass
class HotspotServer:
    name: str
    interface: str
    address_pool: str = "none"
    profile: str = "default"
    idle_timeout: str = "00:05:00"
    keepalive_timeout: str = None
    login_timeout: str = None
    addresses_per_mac: Union[int, str] = None
    copy_from: str = None
    disabled: bool = None
    https: bool = False
    proxy_status: str = None
    id: str = None
    invalid: bool = None

    def __str__(self) -> str:
        return self.name
