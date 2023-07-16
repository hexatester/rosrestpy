from attr import dataclass


@dataclass
class BFDSession:
    multihop: bool
    vrf: str
    remote_address: bool
    local_address: bool
    state: str
    state_changes: int
    uptime: str
    desired_tx_interval: str
    actual_tx_interval: str
    required_min_rx: str
    remote_min_rx: str
    remote_min_tx: str
    multiplier: int
    hold_time: str
    packets_rx: int
    packets_tx: int
    up: bool
