from attr import dataclass
from typing import Literal

MacFormatLiteral = Literal[
    "XX XX XX XX XX XX",
    "XX-XX-XX-XX-XX-XX",
    "XX:XX:XX:XX:XX:XX",
    "XXXX:XXXX:XXXX",
    "XXXXXX-XXXXXX",
    "XXXXXX:XXXXXX",
    "XXXXXXXXXXXX",
]
NASPortLiteral = Literal["cable", "ethernet", "wireless-802.11"]


@dataclass
class HotspotProfile:
    name: str
    hotspot_address: str
    dns_name: str
    html_directory: str
    html_directory_override: str = None
    install_hotspot_queue: bool = True
    rate_limit: str = None
    http_proxy: str = None
    smtp_server: str = None
    login_by: str = None
    mac_auth_mode: str = None
    mac_auth_password: str = None
    http_cookie_lifetime: str = "3d 00:00:00"
    ssl_certificate: str = "none"
    split_user_domain: bool = False
    trial_uptime_limit: str = None
    trial_uptime_reset: str = None
    trial_user_profile: str = None
    use_radius: bool = False
    radius_default_domain: str = None
    radius_location_id: str = None
    radius_location_name: str = None
    radius_mac_format: MacFormatLiteral = "XX:XX:XX:XX:XX:XX"
    radius_accounting: bool = True
    radius_interim_update: str = None
    nas_port_type: NASPortLiteral = "wireless-802.11"
    copy_from: str = None
    id: str = None

    def __str__(self) -> str:
        return self.name
