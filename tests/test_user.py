from ros import Ros, UserModule
from ros.user import User, UserAAA


class TestUser:
    def test_user(self, ros: Ros):
        assert isinstance(ros.user, UserModule)

    def test_get_user(self, ros: Ros):
        for i in ros.user():
            assert isinstance(i, User)


class TestUserAAA:
    def test_user_aaa(self, ros: Ros):
        assert isinstance(ros.user.aaa(), UserAAA)
