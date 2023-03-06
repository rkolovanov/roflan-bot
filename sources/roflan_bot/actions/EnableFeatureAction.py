import re
from typing import Union
from discord import Message
from roflan_bot.actions.common import Action


class EnableFeatureAction(Action):
    def __init__(self, name: str, description: str, access_level: int):
        super().__init__(name, description, access_level)

    @staticmethod
    def recognize_action_name(message: str) -> Union[str, None]:
        match = re.search(r"команд[уе] ([A-Za-z_]+)", message, flags=re.IGNORECASE)
        if match is not None:
            return match[1]
        return None

    async def execute(self, bot, message: Message):
        action_name = self.recognize_action_name(message.content)
        if action_name in bot.actions.keys():
            if action_name not in bot.config["bot"]["actions"].keys():
                bot.config["bot"]["actions"][action_name] = {}

            bot.config["bot"]["actions"][action_name]["enabled"] = True
            bot.config.save_to_file()

            await message.channel.send(bot.get_random_phrase("okay"))
        else:
            await message.channel.send(f"Действие '{action_name}' не существует")
