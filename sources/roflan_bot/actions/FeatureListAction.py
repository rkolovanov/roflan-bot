from roflan_bot.actions.common.Action import Action
from discord import Message


class FeatureListAction(Action):
    def __init__(self, name: str, description: str, access_level: int):
        super(FeatureListAction, self).__init__(name, description, access_level)

    async def execute(self, bot, message: Message):
        data = ["[ Список команд ]"]

        for action_name, action_data in bot.actions.items():
            data.append(f"**{action_name}**")
            data.append(f"  Описание: {action_data['description']}")
            data.append(f"  Уровень доступа: {action_data['access_level']}")
            data.append(f"  Фразы: {action_data['phrases']}")

        await message.channel.send("\n".join(data))
