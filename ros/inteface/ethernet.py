from attr import dataclass


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
    rx_bytes: int
    rx_fcs_error: int
    rx_flow_control: str
    rx_pause: int
    tx_bytes: int
    tx_flow_control: str
    rx_broadcast: int = None
    rx_fragment: int = None
    rx_jabber: int = None
    rx_multicast: int = None
    tx_broadcast: int = None
    tx_multicast: int = None
    tx_pause: int = None
    advertise: str = None
    full_duplex: bool = None
    speed: str = None
    comment: str = None
    fec_mode: str = None
    rx_1024_1518: int = None
    rx_128_255: int = None
    rx_1519_max: int = None
    rx_256_511: int = None
    rx_512_1023: int = None
    rx_64: int = None
    rx_65_127: int = None
    rx_align_error: int = None
    rx_drop: int = None
    rx_length_error: int = None
    rx_packet: int = None
    rx_too_long: int = None
    rx_too_short: int = None
    sfp_rate_select: str = None
    slave: bool = None
    switch: str = None
    tx_1024_1518: int = None
    tx_128_255: int = None
    tx_256_511: int = None
    tx_512_1023: int = None
    tx_64: int = None
    tx_65_127: int = None
    tx_collision: int = None
    tx_deferred: int = None
    tx_drop: int = None
    tx_excessive_collision: int = None
    tx_fcs_error: int = None
    tx_late_collision: int = None
    tx_multiple_collision: int = None
    tx_packet: int = None
    tx_single_collision: int = None
    id: str = None

    def __str__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return not self.disabled
