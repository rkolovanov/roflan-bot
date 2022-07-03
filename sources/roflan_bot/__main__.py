from roflan_bot.bot import BotClient
from roflan_bot.common import Storage, InterClassStorage
import logging
import sys


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout,
                        level=logging.INFO,
                        format="%(asctime)s %(name)s [%(levelname)s]: %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")

    config = Storage(path="../../data/config.json")
    InterClassStorage.set("config", config)

    conversation_settings = Storage(path="../../data/conversation_settings.json")
    InterClassStorage.set("conversation_settings", conversation_settings)

    action = Storage(path="../../data/actions.json")
    InterClassStorage.set("actions", action)

    phrases = Storage(path="../../data/phrases.json")
    InterClassStorage.set("phrases", phrases)

    client = BotClient()
    client.run(config["credentials"]["token"])
