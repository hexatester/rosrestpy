from attr import dataclass


@dataclass(slots=True)
class License:
    software_id: str
    features: str
    nlevel: str
