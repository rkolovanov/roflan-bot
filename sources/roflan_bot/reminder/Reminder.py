from discord.abc import Messageable


class Reminder:
    def __init__(self, channel: Messageable, timestamp: float, message: str):
        self.channel = channel
        self.timestamp = timestamp
        self.message = message
