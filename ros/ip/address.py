from attr import dataclass


@dataclass
class Address:
    address: str
    interface: str
    network: str = None
    comment: str = None
    actual_interface: str = None
    disabled: bool = False
    invalid: str = None
    dynamic: bool = None
    id: str = None

    def __str__(self) -> str:
        return self.address

    def __bool__(self) -> bool:
        return not self.disabled
