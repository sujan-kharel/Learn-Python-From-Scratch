import random


def rollTheDice(randomNum):
    return randomNum * "* "


r = random.randint(1, 6)
print(rollTheDice(r))
