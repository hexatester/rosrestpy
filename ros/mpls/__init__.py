from ros._base import BaseModule, BaseProps

from .ldp import LDP


class MPLSModule(BaseModule):
    _ldp: BaseProps[LDP] = None

    @property
    def ldp(self):
        if not self._ldp:
            self._ldp = BaseProps(self.ros, "/mpls/ldp", LDP)
        return self._ldp
