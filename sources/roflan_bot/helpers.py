import random


def get_random_element(lst: list):
    return lst[random.randint(0, len(lst) - 1)]
