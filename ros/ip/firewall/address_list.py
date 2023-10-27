from attr import dataclass


@dataclass(slots=True)
class IPAddressList:
    """
    Structure:

    ".id": "*CDD",
    "address": "1.2.3.4",
    "creation-time": "2023-10-05 09:47:28",
    "disabled": "false",
    "dynamic": "true",
    "list": "banned",
    "timeout": "1w2d21h26m28s"

    """
    # Required
    list: str
    address: str
    comment: str = None
    disabled: str = None
    timeout: str = None
    creation_time: str = None
    dynamic: str = None
    id: str = None
