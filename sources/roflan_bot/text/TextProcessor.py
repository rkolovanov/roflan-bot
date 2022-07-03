import re


class TextProcessor:
    def __init__(self):
        pass

    @staticmethod
    def replace_characters(text: str, pattern: str, replacement: str = "") -> str:
        text = re.sub(pattern, replacement, text)
        return re.sub(r" +", " ", text).strip(" ")

    @staticmethod
    def simplify_message(message: str) -> str:
        return TextProcessor.replace_characters(message, r"[^A-Za-zА-Яа-я0-9]", " ").lower()

