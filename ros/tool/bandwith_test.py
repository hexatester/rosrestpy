from attr import dataclass


@dataclass(slots=True)
class BandwithTest:
    section: int
    connection_count: int
    direction: str
    lost_packets: int
    random_data: bool
    status: str
    rx_10_second_average: int = None
    rx_current: int = None
    rx_size: int = None
    rx_total_average: int = None
    tx_10_second_average: int = None
    tx_current: int = None
    tx_size: int = None
    tx_total_average: int = None
    about: str = None
    duration: str = None
    local_cpu_load: int = None
    remote_cpu_load: int = None
