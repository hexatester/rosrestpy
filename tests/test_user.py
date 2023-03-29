from ros import Ros, UserModule
from ros.user import User


class TestUser:
    def test_user(self, ros: Ros):
        assert isinstance(ros.user, UserModule)

    def test_get_user(self, ros: Ros):
        for i in ros.user():
            assert isinstance(i, User)
