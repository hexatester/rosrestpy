from attr import dataclass
from typing import Optional, Union


@dataclass
class Interface:
    actual_mtu: int
    disabled: bool
    fp_rx_byte: int
    fp_rx_packet: int
    fp_tx_byte: int
    fp_tx_packet: int
    link_downs: int
    mtu: Union[int, str]
    name: str
    running: bool
    rx_byte: int
    rx_drop: int
    rx_error: int
    rx_packet: int
    tx_byte: int
    tx_drop: int
    tx_error: int
    tx_packet: int
    tx_queue_drop: int
    type: str
    id: str
    comment: Optional[str] = None
    l2mtu: Optional[int] = None
    mac_address: Optional[str] = None
    default_name: Optional[str] = None
    max_l2mtu: Optional[int] = None
    slave: Optional[bool] = None

    def __str__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return not self.disabled
