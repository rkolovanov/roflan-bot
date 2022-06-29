import logging
from roflan_bot.bot import BotClient
from roflan_bot.common import Storage, InterClassStorage


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    InterClassStorage.set("phrases", Storage(path="../../data/phrases.json"))
    InterClassStorage.set("actions", Storage(path="../../data/actions.json"))
    InterClassStorage.set("config", Storage(path="../../data/config.json"))

    config = InterClassStorage.get("config")
    client = BotClient()
    client.run(config["credentials"]["token"])
