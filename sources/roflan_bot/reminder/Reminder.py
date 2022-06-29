import discord
from datetime import datetime
from typing import Union


class Reminder:
    def __init__(self, channel: Union[discord.abc.Messageable], timestamp: datetime, message: str):
        self.channel = channel
        self.timestamp = timestamp
        self.message = message
