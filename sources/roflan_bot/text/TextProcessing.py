import re


class TextProcessing:
    @staticmethod
    def replace(text: str, pattern: str, replacement: str = "") -> str:
        text = re.sub(pattern, replacement, text)
        return re.sub(r" +", " ", text).strip(" ")

    @staticmethod
    def simplify(message: str) -> str:
        return TextProcessing.replace(message, r"[^A-Za-zА-Яа-я0-9]", " ").lower()
