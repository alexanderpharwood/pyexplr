import random


def generateHash():
    return "".join(random.choice('0123456789abcdef') for n in range(24))
