from roflan_bot.actions.common.Action import Action
from roflan_bot.common.InterClassStorage import InterClassStorage
from roflan_bot.helpers import get_random_element
from discord import Message


class GreetingAction(Action):
    def __init__(self, name: str, description: str, access_level: int):
        super(GreetingAction, self).__init__(name, description, access_level)

    async def execute(self, message: Message):
        phrases = InterClassStorage.get("phrases")
        greeting_phrase = get_random_element(phrases["greeting"])
        await message.channel.send(greeting_phrase)
