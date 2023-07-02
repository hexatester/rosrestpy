from attr import dataclass
from typing import Literal, Union
from ros._literals import ARPLiteral


LoopProtectLiteral = Literal["on", "off", "default"]
DontFragmentLiteral = Literal["inherit", "no"]
MTULiteral = Union[str, int]


@dataclass
class EoIP:
    name: str
    remote_address: str = "0.0.0.0"
    tunnel_id = 0
    arp: ARPLiteral = "enabled"
    arp_timeout: str = None
    allow_fast_path: bool = True
    clamp_tcp_mss: bool = True
    disabled: bool = False
    dont_fragment: DontFragmentLiteral = "no"
    dscp: str = "inherit"
    ipsec_secret: str = None
    keepalive: str = "10s,10"
    local_address: str = None
    loop_protect: LoopProtectLiteral = "default"
    loop_protect_disable_time: str = "00:05:00"
    loop_protect_send_interval: str = "00:00:05"
    mac_address: str = None
    mtu: MTULiteral = None
    comment: str = None
    id: str = None
    l2mtu: int = None
    copy_from: str = None
    running: bool = False

    def __str__(self) -> str:
        return self.name
