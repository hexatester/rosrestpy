from attr import dataclass


@dataclass
class IPNeighbor:
    id: str
    interface: str
    address: str
    address4: str
    mac_address: str
    identity: str
    platform: str
    version: str
    age: str
    uptime: str
    software_id: str
    board: str
    interface_name: str
    discovered_by: str
    system_description: str = None
    system_caps: str = None
    system_caps_enabled: str = None
    address6: str = None
    unpack: str = None
