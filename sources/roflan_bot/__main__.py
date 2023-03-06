import logging
import sys
from roflan_bot.common import DataStorage
from roflan_bot.bot import BotClient


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S",
                        format="%(asctime)s %(name)s [%(levelname)s]: %(message)s")

    success = True
    success &= DataStorage.set_actions_data(path="../../data/actions.json")
    success &= DataStorage.set_configuration_data(path="../../data/config.json")
    success &= DataStorage.set_phrases_data(path="../../data/phrases.json")
    success &= DataStorage.set_conversation_settings_data(path="../../data/conversation_settings.json")

    if success:
        client = BotClient()
        client.run(DataStorage.get("config")["credentials"]["token"], log_handler=None)
