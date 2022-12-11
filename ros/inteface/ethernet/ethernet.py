from attr import dataclass
from typing import Optional


@dataclass
class InterfaceEthernet:
    id: str
    advertise: str
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
    full_duplex: bool
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
    rx_1024_1518: int
    rx_128_255: int
    rx_256_511: int
    rx_512_1023: int
    rx_64: int
    rx_65_127: int
    rx_align_error: int
    rx_broadcast: int
    rx_bytes: int
    rx_fcs_error: int
    rx_flow_control: str
    rx_fragment: int
    rx_jabber: int
    rx_multicast: int
    rx_packet: int
    rx_pause: int
    rx_too_long: int
    rx_too_short: int
    speed: str
    switch: str
    tx_1024_1518: int
    tx_128_255: int
    tx_256_511: int
    tx_512_1023: int
    tx_64: int
    tx_65_127: int
    tx_broadcast: int
    tx_bytes: int
    tx_collision: int
    tx_deferred: int
    tx_drop: int
    tx_excessive_collision: int
    tx_fcs_error: int
    tx_flow_control: str
    tx_late_collision: int
    tx_multicast: int
    tx_multiple_collision: int
    tx_packet: int
    tx_pause: int
    tx_single_collision: int
    comment: Optional[str] = None
    slave: Optional[bool] = None

    def __str__(self) -> str:
        return self.name
