from attr import dataclass


@dataclass
class IPPool:
    name: str
    ranges: str
    next_pool: str = None
    comment: str = None
    copy_from: str = None
    id: str = None

    def __str__(self) -> str:
        return self.name
