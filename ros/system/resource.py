from attr import dataclass


@dataclass(slots=True)
class Resource:
    architecture_name: str
    board_name: str
    build_time: str
    cpu: str
    cpu_count: int
    cpu_load: int
    free_hdd_space: int
    free_memory: int
    platform: str
    total_hdd_space: int
    total_memory: int
    uptime: str
    version: str
    bad_blocks: float = None
    cpu_frequency: int = None
    write_sect_since_reboot: int = None
    write_sect_total: int = None
