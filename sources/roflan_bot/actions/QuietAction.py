from roflan_bot.actions.common.Action import Action
from roflan_bot.common.InterClassStorage import InterClassStorage
from roflan_bot.helpers import get_random_element
from discord import Message


class QuietAction(Action):
    def __init__(self, name: str, description: str, access_level: int):
        super(QuietAction, self).__init__(name, description, access_level)

    async def execute(self, message: Message):
        client = InterClassStorage.get("client")
        client.conversation_settings_registry.change_settings(message.channel.id, "silent", True)

        thanks_answer_phrase = get_random_element(client.phrases["okay"])
        await message.channel.send(thanks_answer_phrase)
