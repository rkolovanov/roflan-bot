import copy
import json


class Storage:
    def __init__(self, data: dict = None, path: str = None):
        self._path = path
        self._data = {}

        if data is not None:
            self._data = copy.deepcopy(data)
        elif path is not None:
            self.read_from_file(path)

    def set(self, key: str, value):
        self._data[key] = value

    def get(self, key: str):
        if key in self._data.keys():
            return self._data[key]
        else:
            raise KeyError(f"Секция '{key}' на найдена в хранилище.")

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    def read_from_file(self, path: str = None):
        if path is None:
            path = self._path
        else:
            self._path = path
        try:
            with open(path, mode="r", encoding="utf-8") as file:
                self._data = json.load(file)
        except FileNotFoundError as _:
            self._data = {}
            with open(path, mode="w", encoding="utf-8") as file:
                file.write("{}")

    def save_to_file(self, path: str = None):
        if path is None:
            path = self._path
        try:
            with open(path, mode="w", encoding="utf-8") as file:
                json.dump(self._data, file)
        except FileNotFoundError as error:
            print("Файл не найден:", error)

    def __setitem__(self, key: str, value):
        self.set(key, value)

    def __getitem__(self, key: str):
        return self.get(key)
