import os

import random

import rnd

from character import Character
from format import color, Color

if __name__ == '__main__':
    os.system("")
    print('Welcome to the random people generator!')
    print()
    print('Press <enter> to generate a person or')
    print('enter a citizen id to look up that citizen.')
    print()
    print('Any resemblance to any existing or fictional')
    print('person place or time is purely coincidental.')
    print()

    seedster = random.Random()
    while True:
        i = input('> ').strip()
        if len(i) > 0:
            try:
                s = int(i, 16)
            except Exception:
                print(color(Color.RED, 'sorry, the id you entered seems to be invalid'))
                continue
        else:
            s = seedster.randint(0, 0xFFFFFFFFFFFF)
        rnd.seed(s)
        character = Character()
        print(character.sheet())
        print()
        print(f'citizen id: {color(Color.WHITE, f"{s:08X}")}')
        print()
