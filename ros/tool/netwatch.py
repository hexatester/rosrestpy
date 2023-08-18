from attr import dataclass
from typing import Literal

StatusLiteral = Literal["up", "down", "unknown"]
TypeLiteral = Literal["http-get", "https-get", "icmp", "simple", "tcp-conn"]


@dataclass
class Netwatch:
    host: str
    type: TypeLiteral
    interval: str = None
    timeout: str = None
    start_delay: str = None
    down_script: str = None
    up_script: str = None
    test_script: str = None
    disabled: bool = False
    http_codes: str = None
    port: int = None
    packet_interval: str = None
    packet_count: int = None
    packet_size: int = None
    certificate: str = None
    check_certificate: bool = None
    thr_avg: str = None
    thr_http_time: str = None
    thr_jitter: str = None
    thr_loss_count: str = None
    thr_loss_percent: str = None
    thr_max: str = None
    thr_stdev: str = None
    thr_tcp_conn_time: str = None
    comment: str = None
    status: StatusLiteral = None
    id: str = None
    done_test: int = None
    failed_tests: int = None
    since: str = None
    copy_from: str = None
