import re


def erase_characters(message, pattern):
    message = re.sub(pattern, ' ', message)
    return re.sub(r' +', ' ', message)