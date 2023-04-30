from format import Color, color
from traits.age import Age
from traits.alignment import Alignment
from traits.name import Name
from traits.skillset import SkillSet


class Character:
    def __init__(self):
        self.name = Name(self)
        self.age = Age(self)
        self.skills = SkillSet(self)
        self.alignment = Alignment(self)

    def sheet(self):
        return f'name: {self.name.format(self)}\n' \
               f'age: {self.age.format(self)}\n' \
               f'alignment: {self.alignment.format(self)}\n' \
               f'\n' \
               f'{self.skills.format(self)}'