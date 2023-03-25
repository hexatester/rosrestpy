from attr import dataclass
from typing import Optional


@dataclass
class InterfaceEthernet:
    arp: str
    arp_timeout: str
    auto_negotiation: bool
    bandwidth: str
    default_name: str
    disabled: bool
    driver_rx_byte: int
    driver_rx_packet: int
    driver_tx_byte: int
    driver_tx_packet: int
    l2mtu: int
    loop_protect: str
    loop_protect_disable_time: str
    loop_protect_send_interval: str
    loop_protect_status: str
    mac_address: str
    mtu: int
    name: str
    orig_mac_address: str
    running: bool
    rx_broadcast: int
    rx_bytes: int
    rx_fcs_error: int
    rx_flow_control: str
    rx_fragment: int
    rx_jabber: int
    rx_multicast: int
    rx_pause: int
    tx_broadcast: int
    tx_bytes: int
    tx_flow_control: str
    tx_multicast: int
    tx_pause: int
    id: str = None
    advertise: Optional[str] = None
    full_duplex: Optional[bool] = None
    speed: Optional[str] = None
    comment: Optional[str] = None
    fec_mode: Optional[str] = None
    rx_1024_1518: Optional[int] = None
    rx_128_255: Optional[int] = None
    rx_1519_max: Optional[int] = None
    rx_256_511: Optional[int] = None
    rx_512_1023: Optional[int] = None
    rx_64: Optional[int] = None
    rx_65_127: Optional[int] = None
    rx_align_error: Optional[int] = None
    rx_drop: Optional[int] = None
    rx_length_error: Optional[int] = None
    rx_packet: Optional[int] = None
    rx_too_long: Optional[int] = None
    rx_too_short: Optional[int] = None
    sfp_rate_select: Optional[str] = None
    slave: Optional[bool] = None
    switch: Optional[str] = None
    tx_1024_1518: Optional[int] = None
    tx_128_255: Optional[int] = None
    tx_256_511: Optional[int] = None
    tx_512_1023: Optional[int] = None
    tx_64: Optional[int] = None
    tx_65_127: Optional[int] = None
    tx_collision: Optional[int] = None
    tx_deferred: Optional[int] = None
    tx_drop: Optional[int] = None
    tx_excessive_collision: Optional[int] = None
    tx_fcs_error: Optional[int] = None
    tx_late_collision: Optional[int] = None
    tx_multiple_collision: Optional[int] = None
    tx_packet: Optional[int] = None
    tx_single_collision: Optional[int] = None

    def __str__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return not self.disabled
