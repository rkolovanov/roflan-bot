from roflan_bot.actions.common.Action import Action
from discord import Message


class ThankAction(Action):
    def __init__(self, name: str, description: str, access_level: int):
        super(ThankAction, self).__init__(name, description, access_level)

    async def execute(self, bot, message: Message):
        await message.channel.send(bot.get_random_phrase("thanks_answer"))
