from attr import dataclass


@dataclass
class DHCPRelay:
    id: str
    add_relay_info: bool
    delay_threshold: str
    dhcp_server: str
    disabled: bool
    interface: str
    invalid: bool
    local_address: str
    name: str

    def __str__(self) -> str:
        return self.name
