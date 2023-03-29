from attr import dataclass


@dataclass
class UserSSHKey:
    user: str
    bits: str
    key_owner: str
    RSA: bool
    id: str

    def __str__(self) -> str:
        return self.key_owner or self.user
