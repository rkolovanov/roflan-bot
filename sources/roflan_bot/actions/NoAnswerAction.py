from roflan_bot.actions.common.Action import Action
from discord import Message


class NoAnswerAction(Action):
    def __init__(self, name: str, description: str, access_level: int):
        super(NoAnswerAction, self).__init__(name, description, access_level)

    async def execute(self, bot, message: Message):
        pass
