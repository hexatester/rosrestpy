from attr import dataclass


@dataclass(slots=True)
class Ping:
    avg_rtt: str
    host: str
    max_rtt: str
    min_rtt: str
    packet_loss: int
    received: int
    sent: int
    seq: int
    size: int
    time: str
    ttl: int
