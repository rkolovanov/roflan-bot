from roflan_bot.common.Storage import Storage
import copy
import typing


class ConversationSettingsRegistry:
    def __init__(self, conversation_settings_data: Storage):
        self._conversation_settings_data = conversation_settings_data

    def get_settings(self, conversation_id: str) -> dict:
        if conversation_id in self._conversation_settings_data.keys():
            return self._conversation_settings_data[conversation_id]
        settings = copy.deepcopy(self._conversation_settings_data["default"])
        self._conversation_settings_data[conversation_id] = settings
        self._conversation_settings_data.save_to_file()
        return settings

    def change_settings(self, conversation_id: str, key: str, value: typing.Any):
        self._conversation_settings_data[conversation_id][key] = value
        self._conversation_settings_data.save_to_file()
