import rnd
import colorsys
from format import skillness, extremeness, Color, faded, color


class SkillSet:
    arts_skills = [
        'drawing',
        'painting',
        'sculpting',
        'cooking',
        'decorating'
    ]

    crafts_skills = [
        'chiseling',
        'building',
        'bricklaying',
        'metalworking',
        'woodworking',
        'glassblowing'
    ]

    sports_skills = [
        'ball',
        'hockey',
        'tennis',
        'football',
        'swimming'
    ]

    mental_skills = [
        'thinking',
        'maths',
        'chemistry',
        'herbalism',
        'chess',
    ]

    magic_type = [
        'mage',
        'wizard',
        'witch',
        'magician',
        'paladin',
        'warlock',
        'druid',
        'trickster',
        'enchanter',
        'charlatan',
        'politician'
    ]

    @staticmethod
    def choose_skills(mod, skill_set, skill_color):
        skills = []
        skill_set = skill_set.copy()
        rnd.shuffle(skill_set)
        for i in range(rnd.randint(1, min(int(len(skill_set) * (mod * 1.2 + 0.5)), min(len(skill_set), 6)))):
            if rnd.high() < 1.2 - mod:
                skills.append((color(skill_color, skill_set[i]), rnd.extreme() * (mod + 0.5)))
        return skills

    def __init__(self, character):
        self.skills = []
        self.arts = rnd.extreme() * character.age.rnd_multiplier(False)
        self.skills += SkillSet.choose_skills(self.arts, SkillSet.arts_skills, Color.GOLD)

        self.crafts = rnd.extreme() * character.age.rnd_multiplier(False)
        self.skills += SkillSet.choose_skills(self.crafts, SkillSet.crafts_skills, Color.LIGHT_GREEN)

        self.sports = rnd.extreme() * character.age.rnd_multiplier(True)
        self.skills += SkillSet.choose_skills(self.sports, SkillSet.sports_skills, Color.LIGHT_BLUE)

        self.mental = rnd.extreme() * character.age.rnd_multiplier(False)
        self.skills += SkillSet.choose_skills(self.mental, SkillSet.mental_skills, Color.PINK)
        if rnd.low() > rnd.high() / 2 + 0.2:
            self.is_magic = True
            self.magic = rnd.high()
            self.power = rnd.high() * (self.magic + 0.5)
            self.magic_class = color([int(f * 255) for f in colorsys.hsv_to_rgb(rnd.random(), 1, 1)], rnd.choice(SkillSet.magic_type))
        else:
            self.is_magic = False
            self.magic = 0
            self.power = 0
            self.magic_class = None

    def format(self, character):
        skills_texts = []
        for (skill, value) in self.skills:
            skills_texts.append(f'- is {skillness(value)} at {skill}')
        skills_text = '\n'.join(skills_texts)
        if self.is_magic:
            skills_text += '\n\n' \
                           f'{color(Color.WHITE, character.name.first_name)} is {extremeness(self.magic)} skilled with magic!\n' \
                           f'They are a {extremeness(self.power)} powerful {self.magic_class}.'
        return skills_text
