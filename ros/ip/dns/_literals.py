from typing import Literal

DNSType = Literal[
    "A", "AAAA", "CNAME", "FWD", "MX", "NS", "NXDOMAIN", "PTR", "SRV", "TXT"
]
