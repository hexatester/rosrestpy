from attr import define
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ros.ros import Ros


@define
class BaseModule:
    ros: "Ros"
    url: str = ""

    def __attrs_post_init__(self) -> None:
        self.url = "/" + self.__class__.__name__.lower()
