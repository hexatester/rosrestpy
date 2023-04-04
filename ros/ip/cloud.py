from attr import dataclass


@dataclass(slots=True)
class Cloud:
    ddns_enabled: bool
    ddns_update_interval: str = None
    update_time: bool = None
    public_address: str = None
    status: str = None

    def __bool__(self) -> bool:
        return not self.ddns_enabled
