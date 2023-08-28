from attr import dataclass


@dataclass(slots=True)
class Profile:
    name: str
    usage: float
    section: int

    @property
    def cpu(self) -> int:
        return self.section
