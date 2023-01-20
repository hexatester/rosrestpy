from attr import dataclass


@dataclass(slots=True)
class RouterBOARD:
    current_firmware: str
    factory_firmware: str
    firmware_type: str
    model: str
    routerboard: bool
    serial_number: str
    upgrade_firmware: str
