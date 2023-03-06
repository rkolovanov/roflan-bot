import logging
from roflan_bot.common.Storage import Storage
from roflan_bot.common.StaticStorage import StaticStorage

logger = logging.getLogger(__name__)


class DataStorage(StaticStorage):
    @staticmethod
    def set_actions_data(path: str) -> bool:
        try:
            DataStorage.set("actions", Storage(path=path, create=False))
        except Exception as error:
            logger.critical(f"Ошибка загрузки данных о действиях бота: {error}")
            return False
        finally:
            return True

    @staticmethod
    def set_configuration_data(path: str) -> bool:
        try:
            DataStorage.set("config", Storage(path=path, create=False))
        except Exception as error:
            logger.critical(f"Ошибка загрузки конфигурации бота: {error}")
            return False
        finally:
            return True

    @staticmethod
    def set_phrases_data(path: str) -> bool:
        try:
            DataStorage.set("phrases", Storage(path=path, create=False))
        except Exception as error:
            logger.critical(f"Ошибка загрузки данных о фразах бота: {error}")
            return False
        finally:
            return True

    @staticmethod
    def set_conversation_settings_data(path: str) -> bool:
        try:
            DataStorage.set("conversation_settings", Storage(path=path, create=True))
        except Exception as error:
            logger.critical(f"Ошибка загрузки конфигурации текстовых чатов: {error}")
            return False
        finally:
            return True

    @staticmethod
    def update_data():
        DataStorage.get("actions").read_from_file()
        DataStorage.get("config").read_from_file()
        DataStorage.get("phrases").read_from_file()
        DataStorage.get("conversation_settings").read_from_file()
