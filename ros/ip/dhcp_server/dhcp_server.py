from attr import dataclass
from typing import Optional


@dataclass
class DHCPServer:
    id: str
    add_arp: bool
    address_pool: str
    authoritative: bool
    disabled: bool
    dynamic: bool
    insert_queue_before: str
    interface: str
    invalid: bool
    lease_script: str
    lease_time: str
    name: str
    parent_queue: str
    use_radius: str
    comment: Optional[str] = None

    def __str__(self) -> str:
        return self.name
