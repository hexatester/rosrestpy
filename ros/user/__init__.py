from typing import Any, List
from ros._base import BaseModule, BaseProp, BaseProps

from .aaa import UserAAA
from .user import User


class UserModule(BaseModule):
    _aaa: BaseProp[UserAAA] = None
    _user: BaseProps[User] = None

    @property
    def aaa(self) -> BaseProp[UserAAA]:
        if not self._aaa:
            self._aaa = BaseProp(self.ros, "/user/aaa", UserAAA)
        return self._aaa

    @property
    def user(self) -> BaseProps[User]:
        if not self._user:
            self._user = BaseProps(self.ros, "/user", User)
        return self._user

    def __call__(self, **kwds: Any) -> List[User]:
        return self.user(**kwds)
