from attr import dataclass


@dataclass(slots=True)
class IPScan:
    section: int
    address: str
    dns: str
    netbios: str
    snmp: str
    time: int
