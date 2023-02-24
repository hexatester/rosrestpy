from attr import dataclass
from typing import Optional


@dataclass
class Address:
    address: str
    interface: str
    network: Optional[str] = None
    comment: Optional[str] = None
    actual_interface: Optional[str] = None
    disabled: bool = False
    invalid: Optional[str] = None
    dynamic: Optional[bool] = None
    id: str = None

    def __str__(self) -> str:
        return self.address

    def __bool__(self) -> bool:
        return not self.disabled
