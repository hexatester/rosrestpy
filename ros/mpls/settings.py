from attr import dataclass


@dataclass
class MPLSSettings:
    dynamic_label_range: str
    propagate_ttl: bool
    allow_fast_path: bool
    mpls_fast_path_packets: int
    mpls_fast_path_bytes: int
