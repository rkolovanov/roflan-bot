from roflan_bot.actions.common.Action import Action
from roflan_bot.common.InterClassStorage import InterClassStorage
from discord import Message


class RemindAction(Action):
    def __init__(self, name: str, description: str, access_level: int):
        super(RemindAction, self).__init__(name, description, access_level)

    async def execute(self, message: Message):
        client = InterClassStorage.get("client")
        # TODO: Реализовать
