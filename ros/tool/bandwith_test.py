from attr import dataclass
from typing import Optional


@dataclass(slots=True)
class BandwithTest:
    section: int
    connection_count: int
    direction: str
    lost_packets: int
    random_data: bool
    status: str
    rx_10_second_average: Optional[int] = None
    rx_current: Optional[int] = None
    rx_size: Optional[int] = None
    rx_total_average: Optional[int] = None
    tx_10_second_average: Optional[int] = None
    tx_current: Optional[int] = None
    tx_size: Optional[int] = None
    tx_total_average: Optional[int] = None
    about: Optional[str] = None
    duration: Optional[str] = None
    local_cpu_load: Optional[int] = None
    remote_cpu_load: Optional[int] = None
