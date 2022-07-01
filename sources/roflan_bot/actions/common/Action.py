from discord import Message


class Action:
    def __init__(self, name: str = "None", description: str = "", access_level: int = 0):
        self.name = name
        self.description = description
        self.access_level = access_level

    async def execute(self, message: Message):
        pass
