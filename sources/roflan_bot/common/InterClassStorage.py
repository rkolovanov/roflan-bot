from roflan_bot.common.Storage import Storage
from typing import Any


class InterClassStorage:
    _STORAGE = Storage()

    @staticmethod
    def set(key: str, value: Any) -> None:
        InterClassStorage._STORAGE.set(key, value)

    @staticmethod
    def get(key: str) -> Any:
        return InterClassStorage._STORAGE.get(key)
