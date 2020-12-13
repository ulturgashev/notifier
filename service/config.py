import json


class Config:
    @staticmethod
    def from_file(filename: str):
        data = {}
        with open(filename, "r") as input_file:
            data = json.load(input_file)
        return Config.from_json(data)

    @staticmethod
    def from_json(data: dict):
        config = Config()
        for key, value in data.items():
            setattr(config, key, value)

        return config
