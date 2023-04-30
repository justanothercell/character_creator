from random import choice, random, randint, shuffle, seed


def rnd_neg(value, p=0.5):
    return value if random() < p else -value


def low(e=2):
    r = random()
    return pow(r, e)


def high(e=2):
    r = random()
    return 1 - pow(r, e)


def extreme(e=3):
    return (rnd_neg(high(e=e)) + 1) / 2
