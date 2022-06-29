from roflan_bot.common.Storage import Storage


class InterClassStorage:
    _storage = Storage()

    @staticmethod
    def set(key: str, value):
        InterClassStorage._storage.set(key, value)

    @staticmethod
    def get(key: str):
        return InterClassStorage._storage.get(key)
