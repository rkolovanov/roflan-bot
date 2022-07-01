import discord
from datetime import datetime


class Reminder:
    def __init__(self, channel: discord.abc.Messageable, timestamp: datetime, message: str):
        self.channel = channel
        self.timestamp = timestamp
        self.message = message
