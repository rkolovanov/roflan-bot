import discord
import logging
import traceback
from discord.ext import tasks
from roflan_bot.helpers import get_random_element
from roflan_bot.common import InterClassStorage
from roflan_bot.actions.common.ActionRecognizer import ActionRecognizer
from roflan_bot.actions.common.ActionRegistry import ActionRegistry
from roflan_bot.conversations.ConversationSettingsRegistry import ConversationSettingsRegistry
from roflan_bot.reminder.ReminderHandler import ReminderHandler
from roflan_bot.text.TextAnalyzer import TextAnalyzer
from roflan_bot.text.TextProcessor import TextProcessor


class BotClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._logger = logging.getLogger(__name__)
        self.config = InterClassStorage.get("config")
        self.conversation_settings = InterClassStorage.get("conversation_settings")
        self.actions = InterClassStorage.get("actions")
        self.phrases = InterClassStorage.get("phrases")
        self.action_recognizer = None
        self.action_registry = None
        self.conversation_settings_registry = None
        self.reminder_handler = ReminderHandler()

        self.update_data()

    def update_data(self):
        self.config.read_from_file()
        self.conversation_settings.read_from_file()
        self.actions.read_from_file()
        self.phrases.read_from_file()
        self.action_recognizer = ActionRecognizer(self.actions)
        self.action_registry = ActionRegistry(self.actions)
        self.conversation_settings_registry = ConversationSettingsRegistry(self.conversation_settings)

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
        reminder_loop.start(self)

    async def on_error(self, event: str, *args, **kwargs):
        self._logger.error(f"Error in event '{event}'. Message: {args[0].content}")
        self._logger.error(traceback.format_exc())

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return

        message_content = TextProcessor.simplify_message(message.content)
        if not TextAnalyzer.is_appeal_to_bot(message_content) and message.channel.type != "private":
            return

        self._logger.info(f"Получено сообщение от пользователя '{message.author}' "
                          f"из чата #{message.channel.id} ({message.channel.type}): {message.content}")

        recognized_actions = self.action_recognizer.recognize_actions(message_content)
        conversation_settings = self.conversation_settings_registry.get_settings(message.channel.id)

        if conversation_settings["silent"] and "wake_up" not in recognized_actions:
            return

        if len(recognized_actions) == 0:
            await message.channel.send(self.get_random_phrase("unknown"))

        for action_name in recognized_actions:
            action = self.action_registry.get(action_name)
            await action.execute(message)


@tasks.loop(seconds=1)
async def reminder_loop(client: BotClient):
    expired_reminders = client.reminder_handler.remove_and_get_expired_reminders()

    for reminder in expired_reminders:
        await reminder.channel.send("Напоминаю, что вам нужно {}".format(reminder.message))
