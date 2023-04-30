import rnd
from format import color, Color


class Name:
    with open('data/names/first_names.txt') as fn:
        first_names = [n.strip() for n in fn.readlines()]

    with open('data/names/last_names.txt') as fn:
        last_names = [n.strip() for n in fn.readlines()]

    def __init__(self, character):
        self.first_name = rnd.choice(Name.first_names)
        self.last_name = rnd.choice(Name.last_names)

    def format(self, character):
        return f'{color(Color.WHITE, self.first_name + " " + self.last_name)}'
