import rnd
from format import age_class, Color, color


class Age:
    def __init__(self, character):
        self.age = rnd.randint(1, 20)
        if rnd.random() > 0.5:
            self.age += rnd.randint(0, 35)
            if rnd.random() > 0.5:
                self.age += rnd.randint(0, 35)
                if rnd.random() > 0.5:
                    self.age += int(rnd.low() * 20) + int(rnd.low() * 20)

    def format(self, character):
        return f'{color(Color.WHITE, str(self.age))} ({age_class(self.age)})'

    def rnd_multiplier(self, physical):
        if self.age <= 2:
            return rnd.random() * 0.2 + 0.5
        elif self.age <= 5:
            return rnd.random() * 0.3 + 0.5
        elif self.age <= 12:
            return rnd.low() + 0.5
        elif self.age <= 18:
            return rnd.random() + 0.5
        elif self.age <= 24:
            return rnd.high() + 0.5
        elif self.age <= 45:
            return (rnd.random() if physical else rnd.high()) + 0.5
        elif self.age <= 65:
            return (rnd.low(e=2) if physical else rnd.high()) + 0.5
        elif self.age <= 90:
            return (rnd.low() if physical else rnd.high(e=2)) + 0.5
        else:
            return rnd.random() + 0.5
