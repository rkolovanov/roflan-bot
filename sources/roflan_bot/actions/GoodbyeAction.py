from roflan_bot.actions.common.Action import Action
from roflan_bot.common.InterClassStorage import InterClassStorage
from roflan_bot.helpers import get_random_element
from discord import Message


class GoodbyeAction(Action):
    def __init__(self, name: str, description: str, access_level: int):
        super(GoodbyeAction, self).__init__(name, description, access_level)

    async def execute(self, message: Message):
        client = InterClassStorage.get("client")
        goodbye_phrase = get_random_element(client.phrases["goodbye"])
        await message.channel.send(goodbye_phrase)
