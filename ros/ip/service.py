from attr import dataclass
from typing import Literal

ServiceName = Literal[
    "api", "api-ssl", "ftp", "ssh", "telnet", "winbox", "www", "www-ssl"
]


@dataclass
class Service:
    id: str
    name: ServiceName
    address: str
    port: int
    disabled: bool
    invalid: bool
    vrf: str = None
    certificate: str = None
    tls_version: str = None

    def __str__(self) -> str:
        return self.name
