from attr import dataclass


@dataclass
class HotspotActive:
    id: str
    server: str
    user: str
    address: str
    mac_address: str
    login_by: str
    uptime: str
    session_time_left: str
    keepalive_timeout: str
    comment: str = None
    radius: bool = False
    bytes_in: int = 0
    bytes_out: int = 0
    packets_in: int = 0
    packets_out: int = 0
    idle_time: str = None

    def __str__(self) -> str:
        return self.user
