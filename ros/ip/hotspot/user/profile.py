from attr import dataclass
from typing import Literal, Union

OpenStatusPageLiteral = Literal["always", "http-login"]


@dataclass
class HotspotUserProfile:
    name: str
    address_pool: str = "none"
    session_timeout: str = None
    idle_timeout: str = "none"
    keepalive_timeout: str = "00:02:00"
    status_autorefresh: str = "00:01:00"
    shared_users: Union[int, str] = 1
    rate_limit: str = None
    add_mac_cookie: bool = True
    mac_cookie_timeout: str = "3d 00:00:00"
    address_list: str = None
    incoming_filter: str = None
    outgoing_filter: str = None
    incoming_packet_mark: str = None
    outgoing_packet_mark: str = None
    open_status_page: OpenStatusPageLiteral = "always"
    transparent_proxy: bool = False
    insert_queue_before: str = None
    parent_queue: str = None
    queue_type: str = None
    on_login: str = None
    on_logout: str = None
    advertise: bool = None
    advertise_url: str = None
    advertise_interval: str = None
    advertise_timeout: str = None
    copy_from: str = None
    id: str = None

    def __str__(self):
        return self.name
