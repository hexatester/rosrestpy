from attr import dataclass
from typing import Optional


@dataclass
class UserSSHKey:
    user: str
    bits: str
    key_owner: str
    id: str
    RSA: Optional[bool] = None

    def __str__(self) -> str:
        return self.key_owner or self.user
