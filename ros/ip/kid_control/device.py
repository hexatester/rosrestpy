from attr import dataclass


@dataclass
class Device:
    name: str
    mac_address: str
    user: str
    disabled: bool = None
    copy_from: str = None
    id: str = None
    activity: str = None
    blocked: bool = None
    bytes_down: int = None
    bytes_up: int = None
    dynamic: bool = None
    idle_time: str = None
    inactive: bool = None
    ip_address: str = None
    limited: bool = None
    rate_down: int = None
    rate_up: int = None

    def __str__(self) -> str:
        return self.name
