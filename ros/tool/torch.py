from attr import dataclass
from typing import Optional

from ros._literals import IPProtocol, MACProtocol


@dataclass(slots=True)
class Torch:
    section: int
    rx: int
    rx_packets: int
    tx: int
    tx_packets: int
    cpu: Optional[int] = None
    dscp: Optional[int] = None
    src_port: Optional[str] = None
    dst_port: Optional[str] = None
    ip_protocol: Optional[IPProtocol] = None
    mac_protocol: Optional[MACProtocol] = None
    src_address: Optional[str] = None
    dst_address: Optional[str] = None
