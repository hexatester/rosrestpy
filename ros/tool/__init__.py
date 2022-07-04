from typing import List

from ros._base import BaseModule

from .bandwith_test import BandwithTest
from .ping import Ping


class ToolModule(BaseModule):
    def ping(self, address: str, count: int = 4):
        data = {"address": address, "count": count}
        return self.ros.post_as("/ping", List[Ping], data)

    def bandwith_test(
        self,
        address: str,
        duration: str,
        user: str = None,
        password: str = None,
        protocol: str = "udp",
        direction: str = "receive",
        random_data: bool = False,
    ) -> List[BandwithTest]:
        data = {
            "address": address,
            "duration": duration,
            "user": user,
            "password": password,
            "protocol": protocol,
            "direction": direction,
            "random-data": random_data,
        }
        return self.ros.post_as(self.url + "/bandwidth-test", List[BandwithTest], data)


__all__ = ["BandwithTest", "Ping", "ToolModule"]
