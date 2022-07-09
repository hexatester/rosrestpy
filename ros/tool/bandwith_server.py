from attr import dataclass


@dataclass(slots=True)
class BandwithServer:
    allocate_udp_ports_from: int
    authenticate: bool
    enabled: bool
    max_sessions: int

    def __bool__(self):
        return self.enabled
