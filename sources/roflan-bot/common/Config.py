import json


class Config:
    def __init__(self, path: str):
        self.data = {}

        with open(path, 'r') as file:
            self.data = json.load(file)

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value
