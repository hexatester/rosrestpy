from attr import dataclass
from typing import Literal

QueueKind = Literal[
    "bfifo",
    "cake",
    "codel",
    "fq-codel",
    "mq-pfifo",
    "none",
    "pcq",
    "pfifo",
    "red",
    "sfq",
]
CakeAckFilter = Literal["aggressive", "filter", "none"]
CakeAtm = Literal["atm", "ptm", "none"]
CakeDiffserv = Literal[
    "besteffort", "diffserv3", "diffserv4", "diffserv8", "precedence"
]
CakeFlowmode = Literal[
    "dsthost",
    "dual-dsthost",
    "dual-srchost",
    "flowblind",
    "flows",
    "hosts",
    "srchost",
    "triple-isolate",
]
CakeOverheadScheme = Literal[
    "bridged-llcsnap",
    "bridged-ptm",
    "bridged-vcmux",
    "convervative",
    "docsis",
    "ether-vlan",
    "ethernet",
    "ipoa-llcsnap",
    "ipoa-vcmux",
    "pppoa-llc",
    "pppoa-vcmux",
    "pppoe-llcsnap",
    "pppoe-ptm",
    "pppoe-vcmux",
    "raw",
    "via-ethernet",
    "",
]
CakeRttScheme = Literal[
    "datacentre",
    "internet",
    "interplanetary",
    "lan",
    "metro",
    "none",
    "oceanic",
    "regional",
    "satellite",
]


@dataclass
class QueueType:
    name: str
    kind: QueueKind
    bfifo_limit: int = None
    cake_ack_filter: CakeAckFilter = None
    cake_atm: CakeAtm = None
    cake_autorate_ingress: bool = None
    cake_bandwidth: str = None
    cake_diffserv: CakeDiffserv = None
    cake_flowmode: CakeFlowmode = None
    cake_memlimit: str = None
    cake_mpu: int = None
    cake_nat: bool = None
    cake_overhead: int = None
    cake_overhead_scheme: CakeOverheadScheme = None
    cake_rtt: str = None
    cake_rtt_scheme: CakeRttScheme = None
    cake_wash: bool = None
    codel_ce_threshold: int = None
    codel_ecn: bool = None
    codel_interval: str = None
    codel_limit: int = None
    codel_target: str = None
    fq_codel_ce_threshold: int = None
    fq_codel_ecn: bool = None
    fq_codel_flows: int = None
    fq_codel_interval: str = None
    fq_codel_limit: int = None
    fq_codel_memlimit: int = None
    fq_codel_quantum: int = None
    fq_codel_target: str = None
    mq_pfifo_limit: int = None
    pcq_burst_rate: int = None
    pcq_burst_threshold: int = None
    pcq_burst_time: str = None
    pcq_classifier: str = None
    pcq_dst_address_mask: int = None
    pcq_dst_address6_mask: int = None
    pcq_limit: int = None
    pcq_rate: int = None
    pcq_src_address_mask: int = None
    pcq_src_address6_mask: int = None
    pcq_total_limit: int = None
    pfifo_limit: int = None
    red_avg_packet: int = None
    red_burst: int = None
    red_limit: int = None
    red_max_threshold: int = None
    red_min_threshold: int = None
    sfq_allot: int = None
    sfq_perturb: int = None
    copy_from: str = None
