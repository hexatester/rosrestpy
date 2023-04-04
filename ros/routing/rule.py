from attr import dataclass
from typing import Literal

RuleActions = Literal["drop", "lookup", "lookup-only-in-table", "unreachable"]


@dataclass
class RoutingRule:
    action: RuleActions
    table: str
    dst_address: str = None
    interface: str = None
    src_address: str = None
    min_prefix: str = None
    routing_mark: str = None
    comment: str = None
    disabled: bool = None
    id: str = None
    place_before: str = None
    copy_from: str = None
