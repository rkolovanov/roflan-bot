import re
from typing import Union
from discord import Message
from roflan_bot.actions.common import Action


class WhoIsAction(Action):
    def __init__(self, name: str, description: str, access_level: int):
        super().__init__(name, description, access_level)

    @staticmethod
    def recognize_name(message: str) -> Union[str, None]:
        match = re.search(r"кто такой ([A-Za-zА-Яа-я\d ]+)", message, flags=re.IGNORECASE)
        if match is None:
            return None
        return match[1]

    async def execute(self, bot, message: Message):
        name = self.recognize_name(message.content)

        if name is not None:
            await message.channel.send("{} {} - {}".format(bot.get_random_phrase("think"), name, bot.get_random_phrase("who_is")))
        else:
            await message.channel.send(bot.get_random_phrase("unknown"))
