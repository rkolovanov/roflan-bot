import logging
import traceback
import discord
from random import randint
from discord.ext import tasks
from roflan_bot.common import DataStorage
from roflan_bot.actions.common import ActionRecognizer, ActionRegistry
from roflan_bot.conversations import ConversationSettingsRegistry
from roflan_bot.reminder import ReminderHandler
from roflan_bot.text import TextAnalyzing, TextProcessing

logger = logging.getLogger(__name__)


class BotClient(discord.Client):
    def __init__(self, **kwargs):
        super().__init__(intents=discord.Intents.all(), **kwargs)

        self.config = DataStorage.get("config")
        self.actions = DataStorage.get("actions")
        self.phrases = DataStorage.get("phrases")
        self.conversation_settings = DataStorage.get("conversation_settings")

        self.action_registry = ActionRegistry(self.actions)
        self.action_recognizer = ActionRecognizer(self.actions)
        self.conversation_settings_registry = ConversationSettingsRegistry(self.conversation_settings)
        self.reminder_handler = ReminderHandler()
        self.text_analyzing = TextAnalyzing

    async def on_connect(self):
        logger.info("Подключение установлено.")

    async def on_disconnect(self):
        logger.warning("Подключение потеряно.")

    async def on_ready(self):
        logger.info(f"Бот авторизован как '{self.user}'.")
        reminder_loop.start(self)

    async def on_error(self, event: str, *args, **kwargs):
        logger.error(f"Ошибка в событии '{event}'. {args[0].content}")
        logger.error(traceback.format_exc())

    async def on_message(self, message: discord.Message):
        if not self.need_to_answer(message):
            return

        logger.info(f"Получено сообщение от пользователя '{message.author}' из чата #{message.channel.id} "
                    f"({message.channel.type}): {message.content}")

        message_content = TextProcessing.simplify(message.content)
        recognized_actions = self.action_recognizer.recognize_actions(message_content)
        conversation_settings = self.conversation_settings_registry.get_settings(message.channel.id)

        logger.info(f"Распознанные действия: {', '.join([action for action in recognized_actions])}")

        # Если бот "спит", и ему не говорили просыпаться, то не реагируем
        if conversation_settings["silent"] and "wake_up" not in recognized_actions:
            return

        # Если ни одно действие не распознано, то отвечаем "непониманием"
        if len(recognized_actions) == 0:
            await message.channel.send(self.get_random_phrase("unknown"))

        # TODO: Добавить учет уровня доступа пользователя
        for action_name in recognized_actions:
            if action_name not in self.config["bot"]["actions"].keys():
                self.config["bot"]["actions"][action_name] = {"enabled": True}

            if self.config["bot"]["actions"][action_name]["enabled"]:
                action = self.action_registry.get(action_name)
                await action.execute(self, message)
            else:
                await message.channel.send(self.get_random_phrase("action_disabled"))

    def need_to_answer(self, message: discord.Message) -> bool:
        if message.author.id == self.user.id:
            return False

        message_content = TextProcessing.simplify(message.content)
        if not TextAnalyzing.appeal_to_bot(message_content, self.config["bot"]["names"]):
            if message.channel.type != discord.ChannelType.private:
                return False

        return True

    def update_data(self) -> None:
        DataStorage.update_data()
        self.action_recognizer = ActionRecognizer(self.actions)
        self.action_registry = ActionRegistry(self.actions)
        self.conversation_settings_registry = ConversationSettingsRegistry(self.conversation_settings)

    def get_random_phrase(self, name: str) -> str:
        if name in self.phrases.keys():
            return self.phrases[name][randint(0, len(self.phrases[name]) - 1)]
        return ""


@tasks.loop(seconds=1)
async def reminder_loop(bot: BotClient):
    expired_reminders = bot.reminder_handler.remove_and_get_expired_reminders()

    for reminder in expired_reminders:
        await reminder.channel.send(f"Напоминаю, что вам нужно {reminder.message}")
