from attr import dataclass


@dataclass(slots=True)
class IPAddressList:
    list: str
    address: str
    comment: str = None
    disabled: bool = None
    timeout: str = None
    creation_time: str = None
    dynamic: bool = None
    id: str = None
