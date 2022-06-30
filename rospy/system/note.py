from attr import dataclass


@dataclass
class Note:
    note: str
    show_at_login: bool

    def __str__(self) -> str:
        return self.note
