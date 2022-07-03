from roflan_bot.actions.common.Action import Action
from roflan_bot.reminder.Reminder import Reminder
from datetime import datetime
from discord import Message
import re


class RemindAction(Action):
    def __init__(self, name: str, description: str, access_level: int):
        super(RemindAction, self).__init__(name, description, access_level)

    def recognize_reminder(self, message: Message) -> Reminder or None:
        match = re.search(r"через (.+)", message.content, flags=re.IGNORECASE)
        if match is None:
            return None

        text = match[1]
        recognized = False
        timestamp = datetime.now().timestamp()

        match = re.search(r"(\d+) д(ень|ня|ней) (.*)", text, flags=re.IGNORECASE)
        if match is not None:
            recognized = True
            timestamp += int(match[1]) * 86400
            text = match[3]

        match = re.search(r"(\d+) час(а|ов)? (.*)", text, flags=re.IGNORECASE)
        if match is not None:
            recognized = True
            timestamp += int(match[1]) * 3600
            text = match[3]

        match = re.search(r"(\d+) минут[уы]? (.*)", text, flags=re.IGNORECASE)
        if match is not None:
            recognized = True
            timestamp += int(match[1]) * 60
            text = match[2]

        match = re.search(r"(\d+) секунд[уы]? (.*)", text, flags=re.IGNORECASE)
        if match is not None:
            recognized = True
            timestamp += int(match[1])
            text = match[2]

        if recognized:
            return Reminder(message.channel, timestamp, text)
        else:
            return None

    async def execute(self, bot, message: Message):
        reminder = self.recognize_reminder(message)
        if reminder is None:
            await message.channel.send(bot.get_random_phrase("unknown"))
        else:
            bot.reminder_handler.add(reminder)
            await message.channel.send(bot.get_random_phrase("okay"))
