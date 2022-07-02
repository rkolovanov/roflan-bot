from roflan_bot.actions.common.Action import Action
from roflan_bot.common.InterClassStorage import InterClassStorage
from discord import Message


class FeatureListAction(Action):
    def __init__(self, name: str, description: str, access_level: int):
        super(FeatureListAction, self).__init__(name, description, access_level)

    async def execute(self, message: Message):
        client = InterClassStorage.get("client")
        data = "[ Список команд ]\n"

        for action_name, action_data in client.actions.items():
            data += f"**{action_name}**\n" \
                    f"  Описание: {action_data['description']}\n" \
                    f"  Уровень доступа: {action_data['access_level']}\n" \
                    f"  Фразы: {action_data['phrases']}\n"

        await message.channel.send(data)
