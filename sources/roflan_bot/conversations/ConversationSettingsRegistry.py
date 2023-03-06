from copy import deepcopy
from typing import Any
from roflan_bot.common import Storage


class ConversationSettingsRegistry:
    def __init__(self, conversation_settings_data: Storage):
        self._conversation_settings_data = conversation_settings_data

    def get_settings(self, conversation_id: int) -> dict:
        if str(conversation_id) in self._conversation_settings_data.keys():
            return self._conversation_settings_data[str(conversation_id)]

        settings = deepcopy(self._conversation_settings_data["default"])
        self._conversation_settings_data[str(conversation_id)] = settings
        self._conversation_settings_data.save_to_file()
        return settings

    def change_settings(self, conversation_id: int, key: str, value: Any) -> None:
        self._conversation_settings_data[str(conversation_id)][key] = value
        self._conversation_settings_data.save_to_file()
