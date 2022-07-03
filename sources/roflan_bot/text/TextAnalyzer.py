from roflan_bot.common.InterClassStorage import InterClassStorage


class TextAnalyzer:
    def __init__(self):
        pass

    @staticmethod
    def is_appeal_to_bot(message: str) -> bool:
        config = InterClassStorage.get("config")
        bot_names = config["bot"]["names"]
        split_message = message.split()

        for name in bot_names:
            if name in split_message:
                return True

        return False
