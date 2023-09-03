from attr import dataclass


@dataclass
class LDPInterface:
    interface: str
    hello_interval: str = None
    hold_time: str = None
    transport_addresses: str = None
    accept_dynamic_neighbors: bool = None
    afi: str = None
    comment: str = None
    disabled: bool = None
    copy_from: str = None
    id: str = None
