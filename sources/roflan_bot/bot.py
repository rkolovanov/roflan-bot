import discord
import logging
from discord.ext import tasks
from roflan_bot.helpers import erase_characters, get_random_element
from roflan_bot.common import InterClassStorage
from roflan_bot.actions.common.ActionRecognizer import ActionRecognizer
from roflan_bot.actions.common.ActionRegistry import ActionRegistry
from roflan_bot.reminder.ReminderHandler import ReminderHandler

@tasks.loop(seconds=1)
async def reminder_loop(reminder_handler: ReminderHandler):
    expired_reminders = reminder_handler.remove_and_get_expired_reminders()

    for reminder in expired_reminders:
        await reminder.channel.send("Напоминаю, что вам нужно {}".format(reminder.message))


class BotClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._logger = logging.getLogger(__name__)
        self.config = InterClassStorage.get("config")
        self.actions = InterClassStorage.get("actions")
        self.phrases = InterClassStorage.get("phrases")
        self.action_recognizer = ActionRecognizer(self.actions)
        self.action_registry = ActionRegistry(self.actions)

    def get_random_phrase(self, name: str):
        if name in self.phrases.keys():
            return get_random_element(self.phrases[name])
        return None

    async def on_connect(self):
        self._logger.info("Connected.")

    async def on_disconnect(self):
        self._logger.warning("Connection lost.")

    async def on_ready(self):
        self._logger.info(f"Logged on as '{self.user}'.")
        reminder_loop.start(ReminderHandler())

    async def on_error(self, event: str, *args, **kwargs):
        self._logger.error(f"Error in event '{event}'.")

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return

        self._logger.info(f"Получено сообщение от пользователя '{message.author}': {message.content}")

        text = erase_characters(message.content, r'[^A-Za-zА-Яа-я0-9]').lower()
        enabled_actions = self.config["bot"]["enabled_actions"]

        recognized_actions = self.action_recognizer.recognize_actions(text)
        for action_name in recognized_actions:
            action = self.action_registry.get(action_name)
            await action.execute(message)

        if len(recognized_actions) == 0:
            await message.channel.send(self.get_random_phrase("unknown"))
