import random
import re


def erase_characters(message, pattern):
    message = re.sub(pattern, ' ', message)
    return re.sub(r' +', ' ', message)


def get_random_element(lst: list):
    return lst[random.randint(0, len(lst) - 1)]
