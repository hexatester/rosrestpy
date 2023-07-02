from attr import dataclass


@dataclass
class HotspotHost:
    id: str
    mac_address: str
    address: str
    to_address: str
    server: str
    idle_time: str = None
    uptime: str = None
    host_dead_time: str = None
    idle_timeout: str = None
    bridge_port: str = None
    vlan_id: int = None
    keepalive_timeout: str = None
    bytes_in: int = 0
    packets_in: int = 0
    bytes_out: int = 0
    packets_out: int = 0
    rx_rate: int = 0
    tx_rate: int = 0
    rx_packets: int = 0
    tx_packets: int = 0
    found_by: str = None
    authorized: bool = False
    DHCP: bool = False
    comment: str = None
