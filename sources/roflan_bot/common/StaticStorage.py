from roflan_bot.common.Storage import Storage
from typing import Any


class StaticStorage:
    _STORAGE = Storage()

    @staticmethod
    def set(key: str, value: Any) -> None:
        StaticStorage._STORAGE.set(key, value)

    @staticmethod
    def get(key: str) -> Any:
        return StaticStorage._STORAGE.get(key)
