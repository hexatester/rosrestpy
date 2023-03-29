from attr import dataclass


@dataclass
class UserSettings:
    minimum_password_length: int = 0
    minimum_categories: int = 0
