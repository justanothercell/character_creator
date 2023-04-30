import rnd
from format import extremeness, color, Color


class Alignment:
    ethics_choices = ['lawful', 'neutral', 'chaotic']
    morals_choices = ['good', 'neutral', 'evil']

    def __init__(self, character):
        self.ethics = rnd.choice(Alignment.ethics_choices)
        self.morals = rnd.choice(Alignment.morals_choices)
        self.commitment = rnd.low()
        self.extrovertedness = rnd.random()

    def format(self, character):
        ness = abs(self.extrovertedness-0.5) * 2
        if self.extrovertedness > 0.5:
            ie = 'extroverted'
        else:
            ie = 'introverted'
        if ness > 0.7:
            ie = extremeness((ness-0.7) * 3.4) + ' ' + ie
        return f'{extremeness(self.commitment)+" " if self.commitment > 0.4 else ""}' \
               f'{color(Color.WHITE, self.ethics)} {color(Color.WHITE, self.morals)}' \
               f'{", " + color(Color.WHITE, ie) if ness > 0.2 else ""}'