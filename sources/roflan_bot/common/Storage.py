import json
from copy import deepcopy
from typing import Any, Union


class Storage:
    EMPTY_JSON = "{}"

    def __init__(self, data: dict = None, path: str = None, encoding="utf-8", create=True):
        self._path = path
        self._data = {}
        self._encoding = encoding

        if data is not None:
            self._data = deepcopy(data)
        elif path is not None:
            self.read_from_file(path, create=create)

    def set(self, key: str, value: Any) -> None:
        self._data[key] = value

    def get(self, key: str) -> Any:
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

    def read_from_file(self, path: Union[str, None] = None, create: bool = True) -> None:
        if path is None:
            path = self._path
        else:
            self._path = path

        try:
            with open(path, mode="r", encoding=self._encoding) as file:
                self._data = json.load(file)
        except FileNotFoundError as error:
            if create:
                with open(path, mode="w", encoding=self._encoding) as file:
                    file.write(Storage.EMPTY_JSON)
            else:
                raise error

    def save_to_file(self, path: Union[str, None] = None) -> None:
        if path is None:
            path = self._path

        with open(path, mode="w", encoding=self._encoding) as file:
            json.dump(self._data, file, indent=2)

    def __setitem__(self, key: str, value: Any) -> None:
        self.set(key, value)

    def __getitem__(self, key: str) -> Any:
        return self.get(key)
