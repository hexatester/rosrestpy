from attr import dataclass


@dataclass
class Address:
    id: str
    actual_interface: str
    address: str
    disabled: bool
    dynamic: bool
    interface: str
    invalid: bool
    network: str
