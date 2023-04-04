from attr import dataclass, field
from typing import Literal, Optional

QueuePriority = Literal["0", "1", "2", "3", "4", "5", "6", "7", "8"]


@dataclass
class QueueTree:
    name: str
    parent: str
    packet_mark: str
    queue: str
    priority: QueuePriority = "8"
    bucket_size: float = 0.100
    limit_at: Optional[str] = None
    max_limit: Optional[str] = None
    burst_limit: Optional[str] = None
    burst_threshold: Optional[str] = None
    burst_time: Optional[str] = None
    disabled: Optional[bool] = None
    invalid: Optional[bool] = None
    bytes: Optional[int] = None
    dropped: Optional[int] = None
    queued_bytes: Optional[int] = None
    queued_packets: Optional[int] = None
    rate: Optional[int] = None
    id: str = None
    copy_from: Optional[str] = None
    comment: Optional[str] = None

    def __str__(self) -> str:
        return self.name
