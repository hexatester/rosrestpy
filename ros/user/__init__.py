from typing import Any, List
from ros._base import BaseModule, BaseProp, BaseProps

from .aaa import UserAAA
from .active import UserActive
from .group import UserGroup
from .settings import UserSettings
from .ssh_keys import UserSSHKey
from .user import User


class UserModule(BaseModule):
    _aaa: BaseProp[UserAAA] = None
    _active: BaseProps[UserActive] = None
    _group: BaseProps[UserGroup] = None
    _settings: BaseProp[UserSettings] = None
    _ssh_keys: BaseProps[UserSSHKey] = None
    _user: BaseProps[User] = None

    @property
    def aaa(self) -> BaseProp[UserAAA]:
        if not self._aaa:
            self._aaa = BaseProp(self.ros, "/user/aaa", UserAAA)
        return self._aaa

    @property
    def active(self) -> BaseProps[UserActive]:
        if not self._active:
            self._active = BaseProps(self.ros, "/user/active", UserActive)
        return self._active

    @property
    def group(self) -> BaseProps[UserGroup]:
        if not self._group:
            self._group = BaseProps(self.ros, "/user/group", UserGroup)
        return self._group

    @property
    def settings(self) -> BaseProp[UserSettings]:
        if not self._settings:
            self._settings = BaseProp(self.ros, "/user/settings", UserSettings)
        return self._settings

    @property
    def ssh_keys(self) -> BaseProps[UserSSHKey]:
        if not self._ssh_keys:
            self._ssh_keys = BaseProps(self.ros, "/user/ssh-keys", UserSSHKey)
        return self._ssh_keys

    @property
    def user(self) -> BaseProps[User]:
        if not self._user:
            self._user = BaseProps(self.ros, "/user", User)
        return self._user

    def __call__(self, **kwds: Any) -> List[User]:
        return self.user(**kwds)
