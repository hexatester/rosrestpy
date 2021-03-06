from typing import Optional
from attr import dataclass


@dataclass(slots=True)
class Cloud:
    ddns_enabled: bool
    ddns_update_interval: Optional[str]
    public_address: str
    update_time: bool
    status: Optional[str] = None
