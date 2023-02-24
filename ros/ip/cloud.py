from typing import Optional
from attr import dataclass


@dataclass(slots=True)
class Cloud:
    ddns_enabled: bool
    ddns_update_interval: Optional[str]
    update_time: bool
    public_address: Optional[str] = None
    status: Optional[str] = None

    def __bool__(self) -> bool:
        return not self.ddns_enabled
