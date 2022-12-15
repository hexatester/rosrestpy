from attr import dataclass
from typing import Optional


@dataclass
class DHCPServer:
    id: str
    address_pool: str
    authoritative: bool
    disabled: bool
    dynamic: bool
    interface: str
    invalid: bool
    lease_script: str
    lease_time: str
    name: str
    use_radius: str
    add_arp: Optional[bool] = None
    comment: Optional[str] = None
    insert_queue_before: Optional[str] = None
    parent_queue: Optional[str] = None

    def __str__(self) -> str:
        return self.name
