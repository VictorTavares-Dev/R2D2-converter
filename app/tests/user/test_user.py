from app.user.User import User


def test_success_get_user_name(monkeypatch):
    user = User()
    # Attribute to mock user entry for input() function
    monkeypatch.setattr('builtins.input', lambda _: "Andrea")
    actual_user_name = user.get_user_name()

    assert actual_user_name == "Andrea"

