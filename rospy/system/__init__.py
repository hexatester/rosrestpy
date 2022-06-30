from attr import define
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from rospy.rospy import Rospy

from .identity import Identity
from .resource import Resource


@define
class System:
    rospy: "Rospy"
    url: str = ""

    def __attrs_post_init__(self) -> None:
        self.url = "/" + self.__class__.__name__.lower()

    @property
    def health(self) -> Identity:
        url = self.url + "/" + "health"
        return self.rospy.get_as(url, Identity)

    @property
    def identity(self) -> Identity:
        url = self.url + "/" + "identity"
        return self.rospy.get_as(url, Identity)

    @property
    def resource(self) -> Resource:
        url = self.url + "/" + "resource"
        return self.rospy.get_as(url, Resource)


__all__ = ["Identity", "Resource", "System"]
