from attr import define
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from rospy.rospy import Rospy

from .identity import Identity
from .license import License
from .resource import Resource


@define
class System:
    rospy: "Rospy"
    url: str = ""

    def __attrs_post_init__(self) -> None:
        self.url = "/" + self.__class__.__name__.lower()

    @property
    def health(self) -> Identity:
        return self.rospy.get_as(self.url + "/health", Identity)

    @property
    def identity(self) -> Identity:
        return self.rospy.get_as(self.url + "/identity", Identity)

    @property
    def license(self) -> License:
        return self.rospy.get_as(self.url + "/license", License)

    @property
    def resource(self) -> Resource:
        return self.rospy.get_as(self.url + "/resource", Resource)


__all__ = ["Identity", "Resource", "System"]
