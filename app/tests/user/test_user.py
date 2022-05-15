from app.user.User import User
from app.log.Logger import Logger


def test_success_get_user_name(monkeypatch):
    user = User(logger=Logger())
    # Attribute to mock user entry for input() function
    monkeypatch.setattr('builtins.input', lambda name: "Andrea")
    user.get_user_name()

    assert user.user_name == "Andrea"

