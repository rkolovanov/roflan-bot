from common.Config import Config
from bot import BotClient


if __name__ == "__main__":
    config = Config("../../data/config.json")
    client = BotClient()
    client.run(config["token"])
