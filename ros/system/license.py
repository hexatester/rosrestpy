from attr import dataclass


@dataclass
class License:
    software_id: str
    features: str
    nlevel: str
