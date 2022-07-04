from attr import dataclass


@dataclass(slots=True)
class Error(Exception):
    error: int
    message: str
    detail: str

    def __str__(self) -> str:
        return f"{self.message} ({self.error}): {self.detail}"
