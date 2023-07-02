from attr import dataclass


@dataclass
class HotspotCookie:
    id: str
    user: str
    mac_address: str
    expires_in: str = None
    domain: str = None

    def __str__(self) -> str:
        return self.user
