from attr import dataclass


@dataclass
class UserAAA:
    use_radius: bool
    accounting: bool
    interim_update: str
    default_group: str
    exclude_groups: str
