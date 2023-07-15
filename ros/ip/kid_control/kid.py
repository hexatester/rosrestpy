from attr import dataclass


@dataclass
class KidControl:
    name: str
    sun: str = None
    mon: str = None
    tue: str = None
    wed: str = None
    thu: str = None
    fri: str = None
    sat: str = None
    rate_limit: str = None
    tur_sun: str = None
    tur_mon: str = None
    tur_tue: str = None
    tur_wed: str = None
    tur_thu: str = None
    tur_fri: str = None
    tur_sat: str = None
    disabled: bool = None
    blocked: bool = None
    id: str = None
    copy_from: str = None

    def __str__(self) -> str:
        return self.name
