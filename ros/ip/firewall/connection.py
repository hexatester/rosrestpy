from attr import dataclass

from ros._literals import IPProtocol, TCPState


@dataclass(slots=True)
class IPConnection:
    id: str
    assured: bool
    confirmed: bool
    dst_address: str
    dstnat: bool
    dying: bool
    expected: bool
    fasttrack: bool
    hw_offload: bool
    orig_bytes: int
    orig_fasttrack_bytes: int
    orig_fasttrack_packets: int
    orig_packets: int
    orig_rate: int
    protocol: IPProtocol
    repl_bytes: int
    repl_fasttrack_bytes: int
    repl_fasttrack_packets: int
    repl_packets: int
    repl_rate: int
    reply_dst_address: str
    reply_src_address: str
    seen_reply: bool
    src_address: str
    srcnat: bool
    timeout: str
    connection_mark: str = None
    tcp_state: TCPState = None
