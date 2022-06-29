import discord
import logging
import random
from discord.ext import tasks
from roflan_bot.helpers import erase_characters
from roflan_bot.common import InterClassStorage
from roflan_bot.reminder.ReminderHandler import ReminderHandler


@tasks.loop(seconds=1)
async def reminder_loop(reminder_handler: ReminderHandler):
    expired_reminders = reminder_handler.remove_and_get_expired_reminders()

    for reminder in expired_reminders:
        await reminder.channel.send("Напоминаю, что вам нужно {}".format(reminder.message))


class BotClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.phrases = InterClassStorage.get("phrases")
        self.actions = InterClassStorage.get("actions")
        self.config = InterClassStorage.get("config")

    def get_random_phrase(self, name: str):
        if name in self.phrases.keys():
            return self.phrases[name][random.randint(0, len(self.phrases[name]) - 1)]
        else:
            return None

    async def on_connect(self):
        print("Connected.")

    async def on_disconnect(self):
        print("Connection lost.")

    async def on_ready(self):
        print(f"Logged on as '{self.user}'.")
        reminder_loop.start(ReminderHandler())

    async def on_error(self, event: str, *args, **kwargs):
        print("Error!")

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return

        logging.info(f"Получено сообщение от пользователя '{message.author}': {message.content}")

        text = erase_characters(message, r'[^A-Za-zА-Яа-я0-9]').lower()
        enabled_actions = self.config["bot"]["enabled_actions"]

        # TODO: Выполнение действий через полиморфизм
