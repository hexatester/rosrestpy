from attr import dataclass
from typing import Optional

from ros._literals import MACProtocol


@dataclass(slots=True)
class Torch:
    section: int
    rx: int
    rx_packets: int
    tx: int
    tx_packets: int
    dscp: Optional[int] = None
    src_port: Optional[int] = None
    dst_port: Optional[str] = None
    ip_protocol: Optional[str] = None
    mac_protocol: Optional[MACProtocol] = None
    src_address: Optional[str] = None
    dst_address: Optional[str] = None
