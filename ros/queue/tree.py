from attr import dataclass
from typing import Literal, Union
from ros._base import BaseProps

QueuePriority = Literal["0", "1", "2", "3", "4", "5", "6", "7", "8"]


@dataclass
class QueueTree:
    name: str
    parent: str
    packet_mark: str
    queue: str
    priority: QueuePriority = "8"
    bucket_size: float = 0.100
    limit_at: str = None
    max_limit: str = None
    burst_limit: str = None
    burst_threshold: str = None
    burst_time: str = None
    disabled: bool = None
    invalid: bool = None
    bytes: int = None
    dropped: int = None
    queued_bytes: int = None
    queued_packets: int = None
    rate: int = None
    comment: str = None
    id: str = None
    copy_from: str = None

    def __str__(self) -> str:
        return self.name


class QueueTreeModule(BaseProps[QueueTree]):
    def reset(self, queue: Union[QueueTree, str]):
        rid = queue.id if isinstance(queue, QueueTree) else queue
        self.ros.post_as("/queue/tree/reset", None, {".id": rid})

    def reset_counters(self, queue: Union[QueueTree, str]):
        rid = queue.id if isinstance(queue, QueueTree) else queue
        self.ros.post_as("/queue/tree/reset-counters", None, {".id": rid})

    def reset_counters_all(self):
        self.ros.post_as("/queue/tree/reset-counters-all", None)
