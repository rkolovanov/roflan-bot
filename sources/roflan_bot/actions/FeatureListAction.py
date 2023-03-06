from discord import Message
from roflan_bot.actions.common import Action


class FeatureListAction(Action):
    def __init__(self, name: str, description: str, access_level: int):
        super().__init__(name, description, access_level)

    async def execute(self, bot, message: Message):
        data = ["**СПИСОК КОМАНД:**"]

        for action_name, action_data in bot.actions.items():
            data.append(f"***{action_name}*** - {action_data['description']}")

        await message.channel.send("\n".join(data))
