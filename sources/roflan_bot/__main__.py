import logging
from roflan_bot import BotClient
from roflan_bot.common import Storage, InterClassStorage


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s [%(levelname)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    config = Storage(path="../../data/config.json")
    InterClassStorage.set("config", config)

    action = Storage(path="../../data/actions.json")
    InterClassStorage.set("actions", action)

    phrases = Storage(path="../../data/phrases.json")
    InterClassStorage.set("phrases", phrases)

    client = BotClient()
    InterClassStorage.set("client", client)

    client.run(config["credentials"]["token"])
