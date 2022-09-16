from attr import dataclass
from typing import Optional


@dataclass
class SimpleQueue:
    id: str
    bucket_size: str
    burst_limit: str
    burst_threshold: str
    burst_time: str
    bytes: str
    disabled: bool
    dropped: str
    dynamic: bool
    invalid: bool
    limit_at: str
    max_limit: str
    name: str
    packet_marks: str
    packet_rate: str
    packets: str
    parent: Optional[str]
    priority: str
    queue: str
    queued_bytes: str
    queued_packets: str
    rate: str
    target: str
    total_bytes: int
    total_dropped: int
    total_packet_rate: int
    total_packets: int
    total_queued_bytes: int
    total_queued_packets: int
    total_rate: int
    comment: Optional[str] = None
    dst: Optional[str] = None
    total_queue: Optional[str] = None

    def __str__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return not self.disabled
