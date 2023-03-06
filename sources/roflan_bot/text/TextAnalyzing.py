class TextAnalyzing:
    @staticmethod
    def appeal_to_bot(message: str, bot_names: list[str]) -> bool:
        split_message = message.split()

        for name in bot_names:
            if name.lower() in split_message:
                return True

        return False
