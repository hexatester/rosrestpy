from attr import dataclass


@dataclass
class LDPInstance:
    lsr_id: str
    path_vector_limit: str = None
    hop_limit: str = None
    loop_detect: str = None
    use_explicit_null: str = None
    distribute_for_default: str = None
    transport_addresses: str = None
    vrf: str = None
    afi: str = None
    preferred_afi: str = None
    comment: str = None
    disabled: bool = None
    inactive: bool = None
    copy_from: str = None
    id: str = None
