from attr import dataclass


@dataclass
class RoutingId:
    id: str
    name: str
    select_from_vrf: str
    select_dynamic_id: str
    disabled: bool = False
    comment: str = None
    copy_from: str = None

    def __str__(self) -> str:
        return self.name
