from ros._base import BaseModule, BaseProps

from .configuration import BFDConfiguration
from .session import BFDSession


class BFDModule(BaseModule):
    _configuration: BaseProps[BFDConfiguration] = None
    _session: BaseProps[BFDSession] = None

    @property
    def configuration(self) -> BaseProps[BFDConfiguration]:
        if not self._configuration:
            self._configuration = BaseProps(
                self.ros, "/routing/bfd/configuration", BFDConfiguration
            )
        return self._configuration

    @property
    def session(self) -> BaseProps[BFDSession]:
        if not self._session:
            self._session = BaseProps(self.ros, "/routing/bfd/session", BFDSession)
        return self._session


__all__ = ["BFDConfiguration", "BFDSession", "BFDModule"]
