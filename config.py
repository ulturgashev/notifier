import json


class Config:

    @staticmethod
    def from_json(filename):
        data = {}
        with open(filename, 'r') as input_file:
            data = json.load(input_file)

        config = Config()
        for key, value in data.items():
            setattr(config, key, value)

        return config
