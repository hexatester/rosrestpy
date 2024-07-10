from attr import dataclass


@dataclass
class Note:
    note: str
    show_at_login: bool
    show_at_cli_login: bool = None

    def __str__(self) -> str:
        return self.note
