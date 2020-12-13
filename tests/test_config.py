from service.config import Config


def test_creating_from_json():
    data = {
        "dict": {},
        "string": "str",
        "int": 4,
        "float": 3.4,
    }
    config = Config.from_json(data)
    for key, value in data.items():
        assert getattr(config, key) == value


def test_creating_from_file():
    config = Config.from_file("tests/static/test_config.json")
    assert getattr(config, "CHAT_ID") == 111111111
