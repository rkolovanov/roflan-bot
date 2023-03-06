from discord import Message
from roflan_bot.actions.common import Action


class QuietAction(Action):
    def __init__(self, name: str, description: str, access_level: int):
        super().__init__(name, description, access_level)

    async def execute(self, bot, message: Message):
        bot.conversation_settings_registry.change_settings(message.channel.id, "silent", True)
        await message.channel.send(bot.get_random_phrase("okay"))
