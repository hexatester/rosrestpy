from attr import dataclass


@dataclass
class BridgePort:
    id: str
    nextid: str
    auto_isolate: bool
    bpdu_guard: bool
    bridge: str
    broadcast_flood: bool
    disabled: bool
    dynamic: bool
    edge: str
    fast_leave: bool
    frame_types: str
    horizon: str
    inactive: bool
    ingress_filtering: bool
    interface: str
    internal_path_cost: int
    learn: str
    multicast_router: str
    path_cost: int
    point_to_point: str
    priority: str
    pvid: int
    restricted_role: bool
    restricted_tcn: bool
    status: str
    tag_stacking: bool
    trusted: bool
    unknown_multicast_flood: bool
    unknown_unicast_flood: bool
