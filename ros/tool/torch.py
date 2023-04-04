from attr import dataclass

from ros._literals import IPProtocol, MACProtocol


@dataclass(slots=True)
class Torch:
    section: int
    rx: int
    rx_packets: int
    tx: int
    tx_packets: int
    cpu: int = None
    dscp: int = None
    src_port: str = None
    dst_port: str = None
    ip_protocol: IPProtocol = None
    mac_protocol: MACProtocol = None
    src_address: str = None
    dst_address: str = None
