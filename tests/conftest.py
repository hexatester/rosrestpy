import os
from pytest import fixture
from dotenv import load_dotenv

load_dotenv()

from ros import Ros


@fixture
def server():
    return os.getenv("server")


@fixture
def username():
    return os.getenv("rosuser")


@fixture
def password():
    return os.getenv("password")


@fixture
def ros(server: str, username: str, password: str):
    return Ros(server, username, password)
