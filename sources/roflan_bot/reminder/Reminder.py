from discord.abc import Messageable
from datetime import datetime


class Reminder:
    def __init__(self, channel: Messageable, timestamp: float, message: str):
        self.channel = channel
        self.timestamp = timestamp
        self.message = message
