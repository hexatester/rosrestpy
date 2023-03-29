from typing import Any, List
from ros._base import BaseModule, BaseProps

from .user import User


class UserModule(BaseModule):
    _user: BaseProps[User] = None

    @property
    def user(self) -> BaseProps[User]:
        if not self._user:
            self._user = BaseProps(self.ros, "/user", User)
        return self._user

    def __call__(self, **kwds: Any) -> List[User]:
        return self.user(**kwds)
