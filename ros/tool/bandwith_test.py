from attr import dataclass
from typing import Optional


@dataclass(slots=True)
class BandwithTest:
    section: int
    connection_count: int
    direction: str
    lost_packets: int
    random_data: bool
    rx_10_second_average: int
    rx_current: int
    rx_size: int
    rx_total_average: int
    status: str
    duration: Optional[str] = None
    local_cpu_load: Optional[int] = None
    remote_cpu_load: Optional[int] = None
