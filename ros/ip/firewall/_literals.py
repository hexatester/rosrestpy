from typing import Literal


IPv4Options = Literal[
    "any",
    "loose_source_routing",
    "no_record_route",
    "no_router_alert",
    "no_source_routing",
    "no_timestamp",
    "none",
    "record_route",
    "router_alert",
    "strict_source_routing",
    "timestamp",
]
