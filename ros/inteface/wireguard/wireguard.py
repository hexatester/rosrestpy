from attr import dataclass


@dataclass
class Wireguard:
    name: str
    mtu: int = 1420
    listen_port: int = 13231
    private_key: str = None
    comment: str = None
    disabled: str = False
    copy_from: str = None

    def __str__(self) -> str:
        return self.name
