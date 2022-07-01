from roflan_bot.actions.common.Action import Action
from roflan_bot.common.InterClassStorage import InterClassStorage
from roflan_bot.helpers import get_random_element
from discord import Message


class ThankAction(Action):
    def __init__(self, name: str, description: str, access_level: int):
        super(ThankAction, self).__init__(name, description, access_level)

    async def execute(self, message: Message):
        phrases = InterClassStorage.get("phrases")
        thanks_answer_phrase = get_random_element(phrases["thanks_answer"])
        await message.channel.send(thanks_answer_phrase)
