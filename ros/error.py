from attr import dataclass


@dataclass(slots=True)
class Error(Exception):
    error: int
    message: str
    detail: str = None

    def __str__(self) -> str:
        if self.detail:
            return f"{self.message} ({self.error}): {self.detail}"
        return f"{self.message} ({self.error})"
